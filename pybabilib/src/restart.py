import os
import yaml
import babilib


if __name__ == "__main__":
    work_dir = os.path.dirname(__file__) + "/../"
    hosts_mpv = []

    with open(work_dir + "ip_table.yaml", "r", encoding="utf-8") as fin:
        table_yaml = yaml.safe_load(fin)

    hosts_mpv.append(table_yaml["E7MPV"])
    hosts_mpv.append(table_yaml["J1MPV_main"])
    hosts_mpv.append(table_yaml["J1MPV_sub1"])

    for host in hosts_mpv:
        babilib.restart_mpvbabildes(host)
