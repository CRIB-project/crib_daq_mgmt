#!/bin/bash

current=$(
  cd $(dirname $0)
  pwd
)
datadir=$current/ridf

time=$(date)

# stop signal sending
source "$current/babilib/.venv/bin/activate"
python3 "$current/babilib/src/sto.py"

# get ridf file name
ridf_file=$(ls -lrt "$datadir/*.ridf" | tail -n 1 | awk '{print $9}')
file=${ridf_file##*/}
run_info=${file%.*}

last_line=$(tail -n 1 "$current/log")
if [[ "$last_line" =~ "---" ]]; then
  exit 0
fi

# log setting
is_firstrun=true
shopt -s extglob lastpipe
tac "$current/log" | while read -r line; do
  log=$(echo "$line" | cut -f 2 -s -d "@")
  if [ "$log" = "" ]; then
    continue
  fi

  if [[ "$log" =~ $run_info ]]; then
    echo "${time} stop" >>"$current/log"
  else
    echo "${time} stop   @${run_info}" >>"$current/log"
  fi

  echo "---" >>"$current/log"
  is_firstrun=false
  break
done

if [ $is_firstrun = "true" ]; then
  echo "${time} stop   @${run_info}" >>"$current/log"
  echo "---" >>"$current/log"
fi
