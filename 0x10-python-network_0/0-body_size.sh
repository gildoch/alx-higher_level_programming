#!/bin/bash
# Script that display the size of the body in bytes
curl -si "$1" | grep "Content-Length:" | cut -d ":" -f 2
