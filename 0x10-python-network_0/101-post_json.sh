#!/bin/bash
#print the body of the response with a special header sent in request 
curl -sL -X POST -H "Content-type:application/json" -d @"$2" "$1"
