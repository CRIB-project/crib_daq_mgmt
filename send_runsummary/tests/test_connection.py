import os
import glob
import gspread
from ruamel.yaml import YAML

ERROR_MESSAGE_JSON = "Not found one json key file (neet to put only one)"
ERROR_MESSAGE_CONNECT = "Failed to connect to the spread sheet"


def connect():
    work_dir = os.path.dirname(__file__) + "/../../"
    json_array = glob.glob(work_dir + "send_runsummary/json/*.json")

    yaml = YAML()
    with open(work_dir + "config.yaml", "r", encoding="utf-8") as fin:
        config_yaml = yaml.load(fin)

    in_spread_name = config_yaml["runsummary_config"]["sheetname"]
    os.environ["GSPREAD_SILENCE_WARNINGS"] = "1"
    try:
        gc = gspread.service_account(filename=json_array[0])
        sh_in = gc.open(in_spread_name)
        return 0

    except:
        return 1


def test_json():
    work_dir = os.path.dirname(__file__) + "/../"

    err_flag = 0
    json_array = glob.glob(work_dir + "json/*.json")
    if len(json_array) != 1:
        err_flag = 1
    assert err_flag == 0, ERROR_MESSAGE_JSON


def test_connection():
    err_flag = connect()
    assert err_flag == 0, ERROR_MESSAGE_CONNECT
