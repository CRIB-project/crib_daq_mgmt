import yaml
import babilib
from pathlib import Path


def load_config(config_path):
    """Load and parse the YAML configuration file"""
    with open(config_path, "r", encoding="utf-8") as fin:
        return yaml.safe_load(fin)


def restart_mpv_devices(config):
    """Restart MPV devices based on configuration"""
    for mpv_yaml in config["DAQ_config"]:
        if mpv_yaml["use"] and mpv_yaml["efn"] > 100:
            babilib.restart_mpvbabildes(mpv_yaml["ip_address"])


if __name__ == "__main__":
    work_dir = Path(__file__).parent.parent
    config_path = work_dir / "config.yaml"

    config = load_config(config_path)
    restart_mpv_devices(config)
