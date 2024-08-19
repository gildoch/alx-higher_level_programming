#!/bin/bash
# Script that request and display the status code of the request
curl -sI "$1" | grep "HTTP" | cut -d " " -f 2
