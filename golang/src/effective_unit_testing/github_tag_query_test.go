package main

import (
	"testing"
)

type FakeReleaseInfoGetter struct {
	Tag string
	Err error
}

func (f FakeReleaseInfoGetter) GetLatestReleaseTag(repo string) (string, error) {
	if f.Err != nil {
		return "", f.Err
	}
	return f.Tag, nil
}

type TestCase struct {
	f              FakeReleaseInfoGetter
	repo           string
	expectedTagMsg string
	expectedErr    error
}

func TestGetReleaseTagMessage(t *testing.T) {
	testCases := []TestCase{
		{f: FakeReleaseInfoGetter{Tag: "1.1", Err: nil}, repo: "test/test", expectedTagMsg: "The latest release is 1.1", expectedErr: nil},
		{f: FakeReleaseInfoGetter{Tag: "0.1", Err: nil}, repo: "test/test", expectedTagMsg: "The latest release is 0.1", expectedErr: nil},
	}
	for _, c := range testCases {
		tagMsg, err := getReleaseTagMessage(c.f, c.repo)
		if err != c.expectedErr {
			t.Fatalf("Got unexpected error value %s", err)
		}
		if tagMsg != c.expectedTagMsg {
			t.Fatalf("Expected: %s (%d), Got: %s(%d)", c.expectedTagMsg, len(c.expectedTagMsg), tagMsg, len(tagMsg))
		}
	}
}
