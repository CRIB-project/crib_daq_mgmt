import yaml
import babilib
from pathlib import Path


def load_config(config_path):
    """Load and parse the YAML configuration file"""
    with open(config_path, "r", encoding="utf-8") as fin:
        return yaml.safe_load(fin)


def send_pulses(ip_address, commands):
    """Send pulse commands to MPV device"""
    for cmd in commands:
        babilib.execarg(ip_address, f"mpvctrl {cmd}")


def process_mpv_device(mpv_yaml):
    """Process MPV device based on its configuration"""
    if mpv_yaml["efn"] <= 100:
        return

    ip_address = mpv_yaml["ip_address"]

    if mpv_yaml["ssm_master"]:
        commands = ["nout0 pulse", "nout1 pulse", "pulse 0x1"]
        send_pulses(ip_address, commands)

    if mpv_yaml["ts_master"]:
        commands = ["nout0 pulse", "pulse 0x1"]
        send_pulses(ip_address, commands)


if __name__ == "__main__":
    work_dir = Path(__file__).parent.parent
    config_path = work_dir / "config.yaml"

    config = load_config(config_path)
    for mpv_yaml in config["DAQ_config"]:
        process_mpv_device(mpv_yaml)
