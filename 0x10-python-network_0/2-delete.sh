#!/bin/bash
# Requests a delete from a server and only prints response
curl -X DELETE -sL "$1"
