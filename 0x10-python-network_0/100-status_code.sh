#!/bin/bash
# Script that request and display the status code of the request
curl -so /dev/null --write-out "%{http_code}" "$1"
