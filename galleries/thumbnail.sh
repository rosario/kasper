#!/bin/sh

podman build -t thumbnailer:latest scripts/
podman run --rm -v $(pwd):/mnt -it thumbnailer:latest "/mnt" "http://127.0.0.1:4000/dark-kasper"
