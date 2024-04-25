#!/bin/bash
# Getting the methods that a server allows
curl -sI "$1" | grep Allow | cut -d ' ' -f 2-
