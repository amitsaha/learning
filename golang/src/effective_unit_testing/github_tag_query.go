package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
)

type ReleasesInfo struct {
	Id      uint   `json:"id"`
	TagName string `json:"tag_name"`
}

// Generic Release Info Getter interface
type ReleaseInfoGetter interface {
	GetLatestReleaseTag(string) (string, error)
}

// GitHub's Release Info Getter
type GitHubReleaseInfoGetter struct{}

func (gh GitHubReleaseInfoGetter) GetLatestReleaseTag(repo string) (string, error) {
	apiUrl := fmt.Sprintf("https://api.github.com/repos/%s/releases", repo)
	response, err := http.Get(apiUrl)
	if err != nil {
		return "", err
	}
	defer response.Body.Close()

	body, err := ioutil.ReadAll(response.Body)
	if err != nil {
		return "", err
	}

	releases := []ReleasesInfo{}
	if err := json.Unmarshal(body, &releases); err != nil {
		return "", err
	}
	if len(releases) == 0 {
		return "", fmt.Errorf("No releases found")
	}
	tag := releases[0].TagName
	return tag, nil
}

func getReleaseTagMessage(ri ReleaseInfoGetter, repo string) (string, error) {
	tag, err := ri.GetLatestReleaseTag(repo)
	if err != nil {
		return "", fmt.Errorf("Error fetching release info: %s", err)
	}
	return fmt.Sprintf("The latest release is %s", tag), nil
}

func main() {
	gh := GitHubReleaseInfoGetter{}
	msg, err := getReleaseTagMessage(gh, os.Args[1])
	if err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
	fmt.Println(msg)
}
