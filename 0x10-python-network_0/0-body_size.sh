#!/bin/bash
# displayes tge size the and body of reponse

curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2
