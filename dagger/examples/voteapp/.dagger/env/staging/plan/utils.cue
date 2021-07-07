package main

import (
	"encoding/yaml"

	"dagger.io/dagger/op"
	"dagger.io/dagger"
	"dagger.io/os"
	"dagger.io/docker"
)

// Push a docker image
#DockerPush: {

	repo: string
	tag:  string

	// Image contents
	contents: dagger.#Artifact

	// Optional authentication (FIXME: use dagger secrets)
	auth: {
		username: string
		secret:   string
	}

	// Complete ref after push
	ref: {
		string
		#up: [
			op.#Load & {from: contents},
			op.#DockerLogin & {
				target:   repo
				username: auth.username
				secret:   auth.secret
			},
			op.#PushContainer & {
				ref: "\(repo):\(tag)"
			},
			op.#Export & {
				source: "/dagger/image_ref"
				format: "string"
			},
		]
	}
}

// Load and inspect a compose file in Dagger
#ComposeProject: {
	context: dagger.#Artifact

	filepath: *"docker-compose.yaml" | string

	file: os.#File & {
		from: context
		path: filepath
	}

	spec: {
		services: [string]: {...}
		...
	} // FIXME: enforce full docker compose spec

	spec: yaml.Unmarshal(file.read.data)

	services: spec.services

	// Extract portable container configuration from compose file
	containers: [name=string]: {
		image:   dagger.#Artifact
		command: string | *null
		env: [string]: string
	}

	// Extract a portable subset of the compose file
	containers: {
		for name, svc in services {
			"\(name)": {
				if svc.command != _|_ {
					command: svc.command
				}
				if svc.build != _|_ {
					image: docker.#Build & {
						source: os.#Dir & {
							from: context
							path: svc.build
						}
					}
				}
				if svc.image != _|_ {
					image: docker.#Pull & {
						from: svc.image
					}
				}
				if svc.environment != _|_ {
					env: svc.environment
				}
			}
		}
	}
}
