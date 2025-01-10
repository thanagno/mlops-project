#!/bin/bash

# Get the latest Git commit hash
COMMIT_HASH=$(git rev-parse --short HEAD)

# Build the Docker image
docker build -t thanagnos/my-fastapi:latest .

# Tag the image with the commit hash
docker tag thanagnos/my-fastapi:latest my-image:$COMMIT_HASH

# Push the images
docker push thanagnos/my-fastapi:latest
docker push thanagnos/my-fastapi:$COMMIT_HASH

echo "Image pushed with tags: latest and $COMMIT_HASH"
