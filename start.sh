#!/bin/bash

set -eu

main() {
  local script_dir timestamp
  script_dir=$(dirname "$(realpath "$0")")
  timestamp=$(date)

  # shellcheck disable=SC1091
  source "$script_dir/.venv/bin/activate"
  python "$script_dir/pybabilib/sta.py"

  # Log start time
  echo "${timestamp} start" >>"$script_dir/log"
}

main "$@"
