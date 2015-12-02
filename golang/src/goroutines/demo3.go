// This example demonstrates how we can spawn goroutines to do some work
// and wait for them all to finish. The worker function sends back a value
// after they are done, which we then use to know which goroutine just finished
package main

import (
	"fmt"
	"time"
)

// Number of goroutines to spawn
var NUM_GOROUTINES int = 5 * 100000

func main() {
	// Create a channel of type int which we will be used by the spawned
	// go routines to return their ID
	done := make(chan int)

	// Spawn goroutines
	for i := 1; i <= NUM_GOROUTINES; i++ {
		go doSomething(i, done)
	}
	// Wait to recieve done signals from each goroutine
	for i := 1; i <= NUM_GOROUTINES; i++ {
		fmt.Printf("Worker process %d done\n", <-done)
	}
}

func doSomething(worker int, done chan int) {
	fmt.Printf("Worker process: %d started\n", worker)
	// Do some work
	time.Sleep(100 * time.Millisecond)
	// We are done, send our ID
	done <- worker
}
