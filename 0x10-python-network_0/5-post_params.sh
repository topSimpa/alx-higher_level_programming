#!/bin/bash
#print the body of the response with a special header sent in request 
curl -s -X POST -d 'email=test@gmail.com&subject=I will always be here for PLD' "$1"
