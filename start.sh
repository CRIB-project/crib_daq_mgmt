#!/bin/bash

current=$(
    cd "$(dirname "$0")" || exit 1
    pwd
)
time=$(date)

# shellcheck disable=SC1091
source "$current/pybabilib/.venv/bin/activate"
python "$current/pybabilib/src/sta.py"

# this is DAQ log setting (not necessary)
echo "${time} start" >>"$current/log"
