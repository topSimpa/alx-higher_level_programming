#!/bin/bash
#print the body of the response with a special header sent in request 
curl -s -X POST --data-urlencode @"$2" "$1"
