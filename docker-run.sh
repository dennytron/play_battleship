#!/usr/bin/env bash

docker build -t play_battleship -f Dockerfile .
docker run play_battleship python3.11 main.py
