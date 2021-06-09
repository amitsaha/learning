package main

import (
	"fmt"
	"io/ioutil"
	"log"

	wasm "github.com/wasmerio/wasmer-go/wasmer"
)

func main() {
	wasmBytes, err := ioutil.ReadFile("calc.wasm")
	if err != nil {
		log.Fatal(err)
	}

	engine := wasm.NewEngine()
	store := wasm.NewStore(engine)

	module, _ := wasm.NewModule(store, wasmBytes)

	importObject := wasm.NewImportObject()
	instance, _ := wasm.NewInstance(module, importObject)

	add, err := instance.Exports.GetFunction("add")
	if err != nil {
		log.Fatal(err)
	}

	result, err := add(2, 8)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(result)
}
