import babilib
from ruamel.yaml import YAML


if __name__ == '__main__':
    yaml = YAML()
    with open("ip_table.yaml", "r", encoding="utf-8") as fin:
        table_yaml = yaml.load(fin)

    main_mpv = table_yaml["J1MPV_main"]
	babilib.execarg(main_mpv,'mpvctrl pulse 0x2')
