package main

import (
	"fmt"
	"log"
	"net/http"
	"net/http/cookiejar"
	"net/http/httptest"
	"net/url"
	"testing"

	"golang.org/x/net/publicsuffix"
)

func handlerWithCookie(w http.ResponseWriter, r *http.Request) {
	fmt.Fprint(w, "You got cookies!")
}

func handlerWithoutCookie(w http.ResponseWriter, r *http.Request) {
	fmt.Fprint(w, "No cookies!")
}

func TestClientCookies(t *testing.T) {

	mux := http.NewServeMux()
	mux.HandleFunc("/cookie", handlerWithCookie)
	mux.HandleFunc("/no-cookie", handlerWithoutCookie)
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
}

func TestClientCookiesAfterRedirect(t *testing.T) {

	mux := http.NewServeMux()
	mux.HandleFunc("/cookie", handlerWithCookie)
	mux.HandleFunc("/no-cookie", handlerWithoutCookie)
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
