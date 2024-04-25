#!/bin/bash
# Requests data from a server and returns the size of the body
curl -sI "$1" | grep -i Content-Length | cut -d " " -f 2
