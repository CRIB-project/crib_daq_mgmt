import yaml
import babilib
from pathlib import Path


def load_config(config_path):
    """Load and parse the YAML configuration file"""
    with open(config_path, "r", encoding="utf-8") as fin:
        return yaml.safe_load(fin)


def send_pulse(ip_address):
    """Send pulse command to MPV device"""
    babilib.execarg(ip_address, "mpvctrl pulse 0x2")


def process_mpv_device(mpv_yaml):
    """Process MPV device based on its configuration"""
    if mpv_yaml["ssm_master"] and mpv_yaml["efn"] > 100:
        send_pulse(mpv_yaml["ip_address"])


if __name__ == "__main__":
    work_dir = Path(__file__).parent.parent
    config_path = work_dir / "config.yaml"

    config = load_config(config_path)
    for mpv_yaml in config["DAQ_config"]:
        process_mpv_device(mpv_yaml)
