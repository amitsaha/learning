package main

import (
	"dagger.io/dagger"
)

repo: dagger.#Artifact @dagger(input)

// Load app information from compose file
// Load the docker compose project
compose: #ComposeProject & {
	context: repo
}
