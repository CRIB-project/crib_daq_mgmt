import yaml
import sys
import babilib
from pathlib import Path


def load_config(config_path):
    """Load and parse the YAML configuration file"""
    with open(config_path, "r", encoding="utf-8") as fin:
        return yaml.safe_load(fin)


def set_eb_size(config, size):
    """Set EB size for MPV devices based on configuration"""
    for mpv_yaml in config["DAQ_config"]:
        if mpv_yaml["use"] and mpv_yaml["efn"] > 100:
            ip_address = mpv_yaml["ip_address"]
            babilib.execarg(
                ip_address,
                f"mpvbabicmd {ip_address} setebsize {size}",
            )


def main():
    """Main function"""
    if len(sys.argv) != 2:
        print("usage: python set_EBsize.py [size]")
        sys.exit(1)

    work_dir = Path(__file__).parent.parent
    config_path = work_dir / "config.yaml"

    config = load_config(config_path)
    set_eb_size(config, sys.argv[1])


if __name__ == "__main__":
    main()
