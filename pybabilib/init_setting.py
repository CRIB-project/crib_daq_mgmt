import yaml
from pathlib import Path
from typing import Dict, Any
import subprocess


def print_babicmd(command: str) -> None:
    """Print babirl command with formatting."""
    parts = command.split()
    print(f"\33[1m[babirl command]\33[0m: {' '.join(parts[2:])}")


def run_babicmd(command: str) -> int:
    """Execute babirl command and print its output."""
    try:
        proc = subprocess.run(
            command, shell=True, check=True, text=True, capture_output=True
        )
        print_babicmd(command)
        if proc.stderr:
            print(f"[stderr]: {proc.stderr.strip()}")
        return proc.returncode
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Command failed with exit code {e.returncode}: {command}")
        print(
            f"[stderr]: {e.stderr.strip() if e.stderr else 'No error output available.'}"
        )
        return e.returncode


def set_eflist_status(mpv_config: Dict) -> None:
    """Set eflist status based on config."""
    name = mpv_config["name"]
    efn = mpv_config["efn"]
    ip_address = mpv_config["ip_address"]
    status = "on" if mpv_config["use"] else "off"

    commands = [
        f"babicmd localhost seteflist {efn} del",
        f"babicmd localhost seteflist {efn} add {ip_address} {name}",
        f"babicmd localhost seteflist {efn} {status}",
    ]
    for cmd in commands:
        exit_code = run_babicmd(cmd)
        if exit_code != 0:
            print(f"[WARNING] Command failed: {cmd}")


def load_config(config_path: Path) -> Dict[str, Any]:
    """Load the YAML configuration file."""
    try:
        with config_path.open("r", encoding="utf-8") as fin:
            return yaml.safe_load(fin)
    except FileNotFoundError:
        print(f"[ERROR] Configuration file not found: {config_path}")
        raise
    except yaml.YAMLError as e:
        print(f"[ERROR] Error parsing YAML configuration: {e}")
        raise


def main() -> None:
    """Main function to configure MPVs."""
    work_dir = Path(__file__).parent.parent
    config_path = work_dir / "config.yaml"

    try:
        config_yaml = load_config(config_path)
    except Exception:
        return

    daq_configs = config_yaml.get("DAQ_config", [])
    if not isinstance(daq_configs, list):
        print("[ERROR] Invalid configuration: 'DAQ_config' should be a list.")
        return

    for mpv_config in daq_configs:
        set_eflist_status(mpv_config)


if __name__ == "__main__":
    main()
