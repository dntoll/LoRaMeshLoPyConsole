#!/bin/bash

git add .
git commit -m "OTADeploy"
git push origin main

python3 release_push.py

./clean.sh