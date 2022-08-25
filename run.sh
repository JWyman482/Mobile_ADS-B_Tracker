#!/bin/bash
# run.sh

# echo "Starting Server...";
# ../dump1090/dump1090 --net

echo "Starting Map...";
.venv/bin/activate
python src/app.py
