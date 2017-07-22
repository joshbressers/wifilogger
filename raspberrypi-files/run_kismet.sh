#!/bin/sh

while true; do
timeout -k 3 20 kismet_server -s 2>&1 > /dev/null
done
