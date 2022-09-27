#!/bin/bash
#print the body of the response only if it is 200
curl -sI "$1" | grep "Allow" | cut -d" " -f2
