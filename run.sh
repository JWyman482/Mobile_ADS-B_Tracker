#!/bin/bash
# run.sh
trap "exit" INT TERM ERR
trap "kill 0" EXIT

# echo "Starting Server...";
# ../dump1090/dump1090 --net
~/radar/dump1090/dump1090 --net &

sleep 1s
echo "Starting Map...";
bash ~/radar/Mobile_ADS-B_Tracker/src/.venv/bin/activate
python ~/radar/Mobile_ADS-B_Tracker/src/app.py
