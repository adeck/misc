#!/usr/bin/env bash

set -ex

mkdir venv
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
./convert.py > ../data.csv
deactivate

