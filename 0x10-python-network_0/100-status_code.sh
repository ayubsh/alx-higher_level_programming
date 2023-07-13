#!/bin/bash
# gets http status code
curl -s -o /dev/null -w "%{http_code}" "$1"
