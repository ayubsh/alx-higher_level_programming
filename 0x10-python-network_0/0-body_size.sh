#!/usr/bin/env bash
# displayes tge size the and body of reponse

url="$1"

curl -sI "$url" | grep "Content-Length:" | cut -d " " -f 2
