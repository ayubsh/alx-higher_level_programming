#!/bin/bash
# displayes all http method
curl -sIX OPRIONS "$1" | grep "Allow:" | cut -d " " -f 2-
