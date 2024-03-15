import os
import yaml
import babilib


if __name__ == "__main__":
    work_dir = os.path.dirname(__file__) + "/../../"

    with open(work_dir + "config.yaml", "r", encoding="utf-8") as fin:
        config_yaml = yaml.safe_load(fin)

    for mpv_yaml in config_yaml["MPV_config"]:
        if mpv_yaml["use"]:
            babilib.restart_mpvbabildes(mpv_yaml["ip_address"])
