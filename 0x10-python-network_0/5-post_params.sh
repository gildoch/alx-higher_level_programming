#!/bin/bash
# Script that post to end point and display body response
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
