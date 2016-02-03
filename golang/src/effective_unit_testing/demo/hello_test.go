package main

import (
	"testing"
)
func TestHello(t *testing.T) {
	expectedString := "Hello, testing"
	result := hello()

	if result != expectedString {
		t.Fatalf("Expected %s, Got %s\n", expectedString, result)
	}
}
