package main

import (
	"dagger.io/dagger"
	"dagger.io/aws/s3"
	"dagger.io/netlify"
	"dagger.io/os"
)

repo: dagger.#Artifact @dagger(input)

hello: {

	dir: dagger.#Artifact @dagger(input)

	ctr: os.#Container & {
		command: """
			ls -l /src > /tmp/out
			"""
		mount: "/src": from: dir
	}

	f: os.#File & {
		from: ctr
		path: "/tmp/out"
	}

	message: f.read.data @dagger(output)
}

// Website
web: {
	source: os.#Dir & {
		from: repo
		path: "web"
	}

	url: string @dagger(output)

	// Where to host the website?
	provider: *"s3" | "netlify" @dagger(input)

	// Deploy to AWS S3
	if provider == "s3" {
		url:    "\(bucket.url)index.html"
		bucket: s3.#Put & {
			contentType: "text/html"
			"source":    source
		}
	}

	// Deploy to Netlify
	if provider == "netlify" {
		url: site.url

		site: netlify.#Site & {
			contents: source
		}
	}
}
