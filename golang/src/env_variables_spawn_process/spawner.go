/*
https://gobyexample.com/spawning-processes
https://gobyexample.com/environment-variables

Usage:  
PROGRAM=ls go run spawner.go

*/

package main

import (
	"os"
	"os/exec"
	"fmt"
)

func main() {
	program_name := os.Getenv("PROGRAM")
	spawnedCommand := exec.Command(program_name)

	output, err := spawnedCommand.Output()
	if err != nil {
		panic(err)
	}

	fmt.Println(program_name + "> " )
	fmt.Println(string(output))
}
