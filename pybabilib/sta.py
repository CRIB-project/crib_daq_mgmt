import os
import yaml
import babilib


if __name__ == "__main__":
    work_dir = os.path.dirname(__file__) + "/../../"
    with open(work_dir + "config.yaml", "r", encoding="utf-8") as fin:
        config_yaml = yaml.safe_load(fin)

    for mpv_yaml in config_yaml["DAQ_config"]:
        if mpv_yaml["ssm_master"] and mpv_yaml["efn"] > 100:
            babilib.execarg(mpv_yaml["ip_address"], f"mpvctrl nout0 pulse")
            babilib.execarg(mpv_yaml["ip_address"], f"mpvctrl nout1 pulse")
            babilib.execarg(mpv_yaml["ip_address"], f"mpvctrl pulse 0x1")

        if mpv_yaml["ts_master"] and mpv_yaml["efn"] > 100:
            babilib.execarg(mpv_yaml["ip_address"], f"mpvctrl nout0 pulse")
            babilib.execarg(mpv_yaml["ip_address"], f"mpvctrl pulse 0x1")
