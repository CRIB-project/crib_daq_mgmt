import os
import babilib
import yaml


if __name__ == "__main__":
    work_dir = os.path.dirname(__file__) + "/../"
    with open(work_dir + "config.yaml", "r", encoding="utf-8") as fin:
        config_yaml = yaml.safe_load(fin)

    for mpv_yaml in config_yaml["MPV_config"]:
        if mpv_yaml["ssm_master"]:
            babilib.execarg(mpv_yaml["ip_address"], f"mpvctrl pulse 0x2")
