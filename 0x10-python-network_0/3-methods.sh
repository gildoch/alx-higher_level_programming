#!/bin/bash
# Script that request and display the http method accepted by server
curl -sI "$1" | grep "Allow:" | cut -d " " -f 2-4
