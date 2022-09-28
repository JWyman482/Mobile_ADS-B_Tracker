#!/bin/bash
# run.sh
trap "exit" INT TERM ERR
trap "kill 0" EXIT

# echo "Starting Server...";
# ../dump1090/dump1090 --net
../dump1090/dump1090 --net --interactive &

sleep 1s
echo "Starting Map...";
bash src/.venv/bin/activate
python src/app.py
