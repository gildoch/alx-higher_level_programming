#!/bin/bash
# Script that request and display the http method accepted by server
curl -sI "$1" | grep "Allow:" | sed -ne 's/^Allow: //p'
