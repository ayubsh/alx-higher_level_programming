#!/bin/bash
# displayes all http method
curl -sIX OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-
