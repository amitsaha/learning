#!/bin/bash

# https://golang.org/doc/code.html
workspace=$1/golang
mkdir -p $workspace/src $workspace/pkg $workspace/bin

## update .bash_profile
echo "export GOPATH=$workspace"  >> ~/.bash_profile
echo "export PATH=$PATH:$GOPATH/bin" >> ~/.bash_profile
