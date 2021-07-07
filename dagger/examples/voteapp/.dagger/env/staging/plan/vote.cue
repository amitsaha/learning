package main

import (
	"dagger.io/aws/ecr"
	"dagger.io/gcp/gcr"
)

redis: {
	host: string
	port: int | *36379
}

// Vote service
vote: {
	// URL of the vote service
	url: string @dagger(output)

	// Identifier used by infrastructure setup
	appName: string | *"acme-vote" @dagger(input)

	provider: *"aws" | "google" @dagger(input)

	// Load portable container config from docker compose
	ctr: compose.containers.vote

	if provider == "aws" {
		url: "https://\(hostname)" @dagger(output)

		hostname: "\(appName).acme-764-api.microstaging.io"

		ecrImage: #DockerPush & {
			contents: ctr.image
			repo:     infra.ecrRepository
			tag:      appName
			auth: {
				username: ecrAuth.username
				secret:   ecrAuth.secret
			}
		}

		ecrAuth: ecr.#Credentials & {
			config: infra.awsConfig
		}

		// Creates an ECS Task + Service + deploy via Cloudformation
		app: #ECSApp & {
			awsConfig:      infra.awsConfig
			slug:           appName
			clusterName:    infra.ecsClusterName
			vpcId:          infra.vpcId
			elbListenerArn: infra.elbListenerArn
			"hostname":     hostname
			desiredCount:   1
			container: {
				image: ecrImage.ref
				environment: {
					REDIS_HOST: redis.host
					REDIS_PORT: "36379"
					ctr.env
				}
			}
		}
	}

	if provider == "google" {
		url: "https://\(app.domain)"

		gcrImage: #DockerPush & {
			contents: ctr.image
			repo:     infra.gcrRepository
			tag:      appName
			auth: {
				username: gcrAuth.username
				secret:   gcrAuth.secret
			}
		}

		gcrAuth: gcr.#Credentials & {
			config: infra.gcpConfig
		}

		app: #KubeApp & {
			gcpConfig:   infra.gcpConfig
			name:        appName
			clusterName: infra.gkeClusterName
			image:       gcrImage.ref
			port:        80
			domain:      "\(appName).gke.microstaging.io"
			environment: {
				// FIXME: add redis information
				ctr.env
			}
		}
	}
}
