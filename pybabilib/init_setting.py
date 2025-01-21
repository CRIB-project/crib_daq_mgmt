import os
import yaml
import subprocess

if __name__ == "__main__":
    work_dir = os.path.dirname(__file__) + "/../../"
    with open(work_dir + "config.yaml", "r", encoding="utf-8") as fin:
        config_yaml = yaml.safe_load(fin)

    for mpv_yaml in config_yaml["DAQ_config"]:
        if mpv_yaml["use"]:
            on_off = "on"
        else:
            on_off = "off"

        cmd = f"babicmd localhost seteflist {mpv_yaml["efn"]} {on_off}"
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        _ = proc.communicate()
