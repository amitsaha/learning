package main

import (
	"context"
	"net/http"
	"os"
	"syscall"
	"testing"
	"time"
)

func TestShutdownTimeout(t *testing.T) {

	mux := http.NewServeMux()
	mux.HandleFunc("/api/users", handleUserAPI)
	s := createHTTPServer(":8080", mux)
	go func() {
		s.ListenAndServe()
	}()

	// make a request which will last for longer than 30s
	go func() {
		http.Get("http://localhost:8080/api/users")
	}()

	waitForShutdownCompletion := make(chan struct{})
	go shutDown(context.Background(), &s, waitForShutdownCompletion)

	// sleep for 10 seconds
	time.Sleep(10 * time.Second)

	// send signal to process itself to trigger shutdown
	pid := os.Getpid()
	p, err := os.FindProcess(pid)
	if err != nil {
		t.Fatal(err)
	}

	shutdownStart := time.Now()
	err = p.Signal(syscall.SIGINT)
	<-waitForShutdownCompletion

	if time.Since(shutdownStart) < 30*time.Second {
		t.Fail()
	}
}
