#!/bin/bash

current=$(cd $(dirname $0);pwd)
datadir=$current/ridf

time=$(date)

source $current/babilib/.venv/bin/activate
python3 $current/babilib/src/sto.py

ridf_file=`ls -lrt $datadir/*.ridf | tail -n 1 | awk '{print $9}'`
file=${ridf_file##*/}
run_info=${file%.*}

run_num=`echo $run_info | rev | cut -c -4 | rev`

last_line=`tail -n 1 $current/log`
if [[ "$last_line" =~ "---" ]]; then
  source $current/send_runsummary/.venv/bin/activate
  python3 $current/send_runsummary/src/send_runsummary.py $run_num
  exit 0
fi

flag=true
shopt -s extglob lastpipe
tac $current/log | while read line; do
  log=`echo $line | cut -f 2 -s -d "@"`
  if [ "$log" = "" ]; then
    continue
  fi

  if [[ "$log" =~ "$run_info" ]]; then
    echo "${time} stop" >> $current/log
  else
    echo "${time} stop   @${run_info}" >> $current/log
    source $current/send_runsummary/.venv/bin/activate
    python3 $current/send_runsummary/src/send_runsummary.py $run_num
  fi

  echo "---" >> $current/log
  flag=false
  break
done

if [ $flag = "true" ]; then
  echo "${time} stop   @${run_info}" >> $current/log
  echo "---" >> $current/log
  source $current/send_runsummary/.venv/bin/activate
  python3 $current/send_runsummary/src/send_runsummary.py $run_num
fi
