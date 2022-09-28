#!/bin/bash
#print the size in byte of a response
curl -s -o /dev/null -w %{http_code} "$1"
