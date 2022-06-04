package main

import (
	"log"
	"net/http"
	"net/http/cookiejar"
	"net/http/httptest"
	"net/url"
	"testing"

	"golang.org/x/net/publicsuffix"
)

func TestClientCookies(t *testing.T) {

	mux := http.NewServeMux()
	registerHandlers(mux)

	ts := httptest.NewServer(mux)
	defer ts.Close()

	jar, err := cookiejar.New(&cookiejar.Options{PublicSuffixList: publicsuffix.List})
	if err != nil {
		log.Fatal(err)
	}

	client := &http.Client{
		Jar: jar,
	}

	_, err = client.Get(ts.URL + "/cookie")
	if err != nil {
		t.Fatal(err)
	}

	u, err := url.Parse(ts.URL)
	if err != nil {
		t.Fatal(err)
	}
	for _, cookie := range jar.Cookies(u) {
		if cookie.Name == "my-cookie" {
			return
		}
	}
	t.Fatalf("Couldn't find cookie, my-cookie after request to /cookie")

	_, err = client.Get(ts.URL + "/check-cookie")
	if err != nil {
		t.Fatal(err)
	}

	u, err = url.Parse(ts.URL)
	if err != nil {
		t.Fatal(err)
	}
	for _, cookie := range jar.Cookies(u) {
		if cookie.Name == "cookie-found" {
			return
		}
	}
	t.Fatalf("Couldn't find cookie, cookie-found after request to /check-cookie")
}

func TestClientCookiesAfterRedirect(t *testing.T) {

	mux := http.NewServeMux()
	registerHandlers(mux)

	ts := httptest.NewServer(mux)
	defer ts.Close()

	jar, err := cookiejar.New(&cookiejar.Options{PublicSuffixList: publicsuffix.List})
	if err != nil {
		log.Fatal(err)
	}

	client := &http.Client{
		Jar: jar,
	}

	_, err = client.Get(ts.URL + "/no-cookie")
	if err != nil {
		t.Fatal(err)
	}

	u, err := url.Parse(ts.URL)
	if err != nil {
		t.Fatal(err)
	}
	for _, cookie := range jar.Cookies(u) {
		if cookie.Name == "my-redirect-cookie" {
			return
		}
	}
	t.Fatalf("Couldn't find cookie, my-redirect-cookie after request to /cookie")
}
