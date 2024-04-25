#!/bin/bash
# Requests data (GET) from a server and only prints OK responses
curl -X GET -sL "$1"
