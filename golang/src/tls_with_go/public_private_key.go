package main

import (
	"crypto/rand"
	"crypto/rsa"
	"fmt"
	"log"
	"strconv"
)

func main() {
	privKey, err := rsa.GenerateKey(rand.Reader, 2048)
	if err != nil {
		log.Fatalf("Generating random key: %v", err)
	}

	plainText := []byte("This is a line of text")
	// Encrypt the plain text above
	cipherText, err := rsa.EncryptPKCS1v15(rand.Reader, &privKey.PublicKey, plainText)
	if err != nil {
		log.Fatalf("Could not encrypt data: %v", err)
	}
	fmt.Printf("%s\n", strconv.Quote(string(cipherText)))

	// Decrypt the cipher text
	decryptedText, err := rsa.DecryptPKCS1v15(nil, privKey, cipherText)
	if err != nil {
		log.Fatalf("Could not encrypt data: %v", err)
	}
	fmt.Printf("%s\n", decryptedText)

}
