#!/bin/bash
# sends post requitest with json data
curl -sX POST -H "Content-Type: application/json" -d "@$2" "$1"
