#!/bin/bash
# run.sh

# echo "Starting Server...";
# ../dump1090/dump1090 --write-json ../Mobile_ADS-B_Tracker/data/ > /dev/null 2>&1 &

echo "Starting Map...";
. ./env/bin/activate
. environment.sh
python src/app.py
