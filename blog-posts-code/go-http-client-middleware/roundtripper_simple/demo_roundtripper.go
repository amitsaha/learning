package main

import (
	"net/http"
)

type demoRoundTripper struct{}

func (t *demoRoundTripper) RoundTrip(r *http.Request) (*http.Response, error) {
	return http.DefaultTransport.RoundTrip(r)
}
