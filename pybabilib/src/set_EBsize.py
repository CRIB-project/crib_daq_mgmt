import os
import yaml
import sys
import babilib


if __name__ == "__main__":
    work_dir = os.path.dirname(__file__) + "/../"
    args = sys.argv
    if len(args) != 2:
        print("usage: python set_EBsize.py [size]")
        sys.exit()

    with open(work_dir + "config.yaml", "r", encoding="utf-8") as fin:
        config_yaml = yaml.safe_load(fin)

    for mpv_yaml in config_yaml["MPV_config"]:
        if mpv_yaml["use"]:
            babilib.execarg(mpv_yaml["ip_address"], f"mpvbabicmd {mpv_yaml["ip_address"]} setebsize {args[1]}")
