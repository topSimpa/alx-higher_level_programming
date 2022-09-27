#!/bin/bash
#print the body of the response with a special header sent in request 
curl -s -H "X-School-User-Id: 98" "$1"
