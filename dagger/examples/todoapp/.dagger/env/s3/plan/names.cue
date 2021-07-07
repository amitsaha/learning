package main

import (
	"strings"

	"dagger.io/os"
	"dagger.io/docker"
)

#image: "public.ecr.aws/j7f8d3t2/funny-names:latest@sha256:3bd1a1225bb9a464bd468dfc6486f55f133cc2fa40fe1a08a094aa8810d93054"

funnyName: (os.#File & {
	from: os.#Container & {
		image: docker.#Pull & {
			from: #image
		}
		command: "/app/main > /out"
	}
	path: "/out"
}).read.data

// Application Name
appName: strings.Trim(funnyName, "\n") @dagger(output)
