#!/bin/bash

set -eu

# Constants
SCRIPT_DIR=$(dirname "$(realpath "$0")")
readonly SCRIPT_DIR
readonly LOG_FILE="$SCRIPT_DIR/log"
readonly RIDF_DIR="$SCRIPT_DIR/ridf"

send_stop_signal() {
  # shellcheck disable=SC1091
  source "$SCRIPT_DIR/.venv/bin/activate"
  python "$SCRIPT_DIR/pybabilib/sto.py"
}

get_latest_run_info() {
  local ridf_file
  if ! compgen -G "$RIDF_DIR/*.ridf" >/dev/null; then
    return 0
  fi
  ridf_file=$(find "$RIDF_DIR"/*.ridf | sort -nr | head -n 1)
  basename "${ridf_file%.*}"
}

append_log() {
  local timestamp run_info="$1"
  timestamp=$(date)

  # Check if last line is separator
  local last_line
  last_line=$(tail -n 1 "$LOG_FILE")
  [[ "$last_line" =~ "---" ]] && exit 0

  # Handle empty run_info case
  if [[ -z "$run_info" ]]; then
    echo "${timestamp} stop" >>"$LOG_FILE"
    echo "---" >>"$LOG_FILE"
    return
  fi

  # Find matching run in log
  local found_match=false
  local log_entry
  shopt -s lastpipe
  tac "$LOG_FILE" | while read -r line; do
    log_entry=$(echo "$line" | cut -f 2 -s -d "@")
    [[ -z "$log_entry" ]] && continue

    if [[ "$log_entry" =~ $run_info ]]; then
      echo "${timestamp} stop" >>"$LOG_FILE"
    else
      echo "${timestamp} stop   @${run_info}" >>"$LOG_FILE"
    fi
    echo "---" >>"$LOG_FILE"
    found_match=true
    break
  done

  # Handle first run case
  if ! $found_match; then
    echo "${timestamp} stop   @${run_info}" >>"$LOG_FILE"
    echo "---" >>"$LOG_FILE"
  fi
}

main() {
  send_stop_signal
  append_log "$(get_latest_run_info)"
}

main "$@"
