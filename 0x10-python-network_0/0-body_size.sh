#!/usr/bin/bash
#print the size in byte of a response
curl -sI "$1" | grep "Content-Length" | cut -d" " -f2
