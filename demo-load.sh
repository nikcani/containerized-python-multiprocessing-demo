#!/usr/bin/env bash

clear && docker run "$(docker build -q .)" python demo-load.py