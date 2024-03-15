#!/bin/bash

current=$(
    cd "$(dirname "$0")" || exit 1
    pwd
)
time=$(date)

echo "${time} start" >>"$current/log"

source "$current/pybabilib/.venv/bin/activate"
python "$current/pybabilib/src/sta.py"
