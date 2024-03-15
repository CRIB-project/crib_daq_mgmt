import pytest
import os
import yaml

def get_yaml():
    work_dir = os.path.dirname(__file__) + "/../"
    with open(work_dir + "config.yaml", "r", encoding="utf-8") as fin:
        config_yaml = yaml.safe_load(fin)
    return config_yaml

def test_ssm():
    config_yaml = get_yaml()
    count = 0
    for mpv_yaml in config_yaml["MPV_config"]:
        if mpv_yaml["ssm_master"]:
            count += 1
    assert count == 1, "Number of SSM Master MPV is not 1!"

def test_ts():
    config_yaml = get_yaml()
    count = 0
    for mpv_yaml in config_yaml["MPV_config"]:
        if mpv_yaml["ts_master"]:
            count += 1
    assert count <= 1, "Number of TS Master MPV is over 1!"
