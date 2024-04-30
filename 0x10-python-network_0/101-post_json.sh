#!/bin/bash
# Sends a JSON POST request to a url passed as first arg, and display's response body 
curl -s -H "Content-Type: application/json" -X POST -d @"$2" "$1"
