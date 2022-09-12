package main

import (
	"io"
	"log"
	"net/http"
)

func makeRequest(client *http.Client, url string) {

	log.Printf("Sending GET request to: %s\n", url)
	resp, err := client.Get(url)
	if err != nil {
		log.Println(err)
	}
	if resp != nil {
		data, err := io.ReadAll(resp.Body)
		if err != nil {
			log.Println(err)
		}
		log.Println(string(data))
		resp.Body.Close()
	}
}

func main() {
	client := http.Client{
		Transport: &demoRoundTripper{},
	}
	makeRequest(&client, "https://example.com")
}
