#!/bin/bash
#print the size in byte of a response
curl -sl -o /dev/null -w "You got me!" 0.0.0.0:5000/catch_me
