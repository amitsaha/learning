#!/bin/bash

# https://golang.org/doc/code.html
workspace=$1/golang
mkdir -p $workspace/src $workspace/pkg $workspace/bin

## update .bashrc
echo "export GOPATH=$workspace"  >> ~/.bashrc
echo "export PATH=$PATH:$GOPATH/bin" >> ~/.bashrc
