#!/bin/bash
# Script that send a file in post
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
