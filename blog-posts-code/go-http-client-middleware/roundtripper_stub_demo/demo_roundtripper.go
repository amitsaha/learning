package main

import (
	"errors"
	"io"
	"net/http"
	"strings"
)

type demoRoundTripper struct{}

func (t *demoRoundTripper) RoundTrip(r *http.Request) (*http.Response, error) {
	switch r.URL.String() {
	case "https://github.com":
		responseBody := "This is github.com stub"
		respReader := io.NopCloser(strings.NewReader(responseBody))
		resp := http.Response{
			StatusCode:    http.StatusOK,
			Body:          respReader,
			ContentLength: int64(len(responseBody)),
			Header: map[string][]string{
				"Content-Type": {"text/plain"},
			},
		}
		return &resp, nil

	case "https://example.com":
		return http.DefaultTransport.RoundTrip(r)

	default:
		return nil, errors.New("Request URL not supported by stub")
	}
}
