package main

import (
	"crypto"
	"crypto/rand"
	"crypto/rsa"
	"crypto/sha256"
	"fmt"
	"log"
)

func main() {
	privKey, err := rsa.GenerateKey(rand.Reader, 2048)
	if err != nil {
		log.Fatalf("Generating random key: %v", err)
	}

	plainText := []byte("This is a line of text")
	hash := sha256.Sum256(plainText)
	fmt.Printf("The hash of the message is: %#x\n", hash)

	// Generate a signature using the private key
	signature, err := rsa.SignPKCS1v15(rand.Reader, privKey, crypto.SHA256, hash[:])
	if err != nil {
		log.Fatalf("Error creating signature: %v", err)
	}

	// Use a public key to verify the signature for a message was created by
	// the private key
	verify := func(pub *rsa.PublicKey, msg, signature []byte) error {
		hash := sha256.Sum256(msg)
		return rsa.VerifyPKCS1v15(pub, crypto.SHA256, hash[:], signature)
	}
	fmt.Println(verify(&privKey.PublicKey, plainText, []byte("A bad signature")))
	fmt.Println(verify(&privKey.PublicKey, []byte("A different plain text"), signature))
	fmt.Println(verify(&privKey.PublicKey, plainText, signature))
}
