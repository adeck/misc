#!/usr/bin/env bash

set -ex

# Added this check to prevent data from being overwritten, just in case.
datafile=../data.csv
[[ -f "$datafile" ]] && {
    echo "file '$datafile' already exists. Doing nothing."
} || {
    mkdir venv
    python3 -m venv venv
    . venv/bin/activate
    pip install -r requirements.txt
    ./convert.py > ../data.csv
    deactivate
}

