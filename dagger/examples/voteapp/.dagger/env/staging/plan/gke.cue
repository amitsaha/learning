package main

import (
	"encoding/yaml"
	"strings"

	"dagger.io/gcp"
	"dagger.io/gcp/gke"

	"dagger.io/kubernetes"
)

#KubeApp: {
	name:  string
	image: string
	environment: [string]: string
	port:        int
	gcpConfig:   gcp.#Config
	clusterName: string
	domain:      string

	resources: {
		deployment: {
			apiVersion: "apps/v1"
			kind:       "Deployment"
			metadata: {
				"name": name
				labels: app: name
			}
			spec: {
				replicas: 1
				selector: matchLabels: app: name
				template: {
					metadata: labels: app: name
					spec: containers: [{
						"name":  name
						"image": image
						env: [ for k, v in environment {name: k, value: v}]
						ports: [{
							containerPort: port
						}]
					}]
				}
			}
		}

		service: {
			apiVersion: "v1"
			kind:       "Service"
			metadata: "name": name
			spec: {
				selector: app: name
				ports: [{
					targetPort: port
					"port":     port
				}]
			}
		}

		ingress: {
			apiVersion: "extensions/v1beta1"
			kind:       "Ingress"
			metadata: {
				"name": name
				annotations: {
					"cert-manager.io/cluster-issuer":            "letsencrypt"
					"kubernetes.io/ingress.class":               "nginx"
					"acme.cert-manager.io/http01-edit-in-place": "true"
				}
			}
			spec: {
				tls: [{
					hosts: [domain]
					secretName: "\(name)-cert"
				}]
				rules: [{
					host: domain
					http: paths: [{
						backend: {
							serviceName: name
							servicePort: port
						}
					}]
				}]
			}
		}
	}

	auth: gke.#KubeConfig & {
		config:        gcpConfig
		"clusterName": clusterName
	}

	// Apply deployment
	deploy: kubernetes.#Apply & {
		kubeconfig: auth.kubeconfig
		namespace:  "dagger-example"
		manifest:   strings.Join([
				yaml.Marshal(resources.deployment),
				yaml.Marshal(resources.service),
				yaml.Marshal(resources.ingress),
		], "---\n")
	}
}
