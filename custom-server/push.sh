#!/usr/bin/env bash
IMAGE_TAG=0.0.1
docker build -t yourdockerusername/demo-seldon:$IMAGE_TAG .
docker push yourdockerusername/demo-seldon:$IMAGE_TAG