import os
import yaml
import babilib


if __name__ == "__main__":
    work_dir = os.path.dirname(__file__) + "/../"
    with open(work_dir + "ip_table.yaml", "r", encoding="utf-8") as fin:
        table_yaml = yaml.safe_load(fin)

    main_mpv = table_yaml["J1MPV_main"]

    babilib.execarg(main_mpv, "mpvctrl nout0 pulse")
    babilib.execarg(main_mpv, "mpvctrl nout1 pulse")
    babilib.execarg(main_mpv, "mpvctrl pulse 0x1")
