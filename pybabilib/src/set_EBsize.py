import os
from ruamel.yaml import YAML
import sys
import babilib


if __name__ == "__main__":
    work_dir = os.path.dirname(__file__) + "/../"
    args = sys.argv
    if len(args) != 2:
        print("usage: python3 set_EBsize.py size")
        sys.exit()

    hosts_mpv = []

    yaml = YAML()
    with open(work_dir + "ip_table.yaml", "r", encoding="utf-8") as fin:
        table_yaml = yaml.load(fin)

    hosts_mpv.append(table_yaml["E7MPV"])
    hosts_mpv.append(table_yaml["J1MPV_main"])
    hosts_mpv.append(table_yaml["J1MPV_sub1"])

    for host in hosts_mpv:
        babilib.execarg(host, "mpvbabicmd " + str(host) + " setebsize " + str(args[1]))
