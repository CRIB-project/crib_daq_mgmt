import os
from ruamel.yaml import YAML
import babilib


if __name__ == "__main__":
    work_dir = os.path.dirname(__file__) + "/../"
    hosts_mpv = []

    yaml = YAML()
    with open(work_dir + "ip_table.yaml", "r", encoding="utf-8") as fin:
        table_yaml = yaml.load(fin)

    hosts_mpv.append(table_yaml["E7MPV"])
    hosts_mpv.append(table_yaml["J1MPV_main"])
    hosts_mpv.append(table_yaml["J1MPV_sub1"])

    for host in hosts_mpv:
        babilib.restart_mpvbabildes(host)
