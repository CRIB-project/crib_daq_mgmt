import sys
import glob
import os
import subprocess
import re
import gspread
import time
from ruamel.yaml import YAML


class Sender:
    __work_dir = os.path.dirname(__file__) + "/../../"
    __run_min = -1
    __run_max = -1
    __all = False

    def __init__(self, args):
        if len(args) == 1:
            self.__all = True
        elif len(args) == 2:
            self.__run_min = int(args[1])
            self.__run_max = int(args[1])
        elif len(args) == 3:
            self.__run_min = int(args[1])
            self.__run_max = int(args[2])
            if self.__run_max < self.__run_min:
                self.__run_min, self.__run_max = self.__run_max, self.__run_min
        else:
            self.usage()
            sys.exit(1)

        yaml = YAML()
        with open(self.__work_dir + "config.yaml", "r", encoding="utf-8") as fin:
            config_yaml = yaml.load(fin)

        self.__spread_name = config_yaml["runsummary_config"]["sheetname"]
        self.__path_prinfo = config_yaml["runsummary_config"]["prinfo"]
        self.__path_data = self.__work_dir + "ridf/"

        self.set_worksheet()

    def usage(self) -> None:
        print("ERROR: input error or there are no such ridf file")
        print("USAGE: python send_runsummary.py [runnumber]")
        print("       python send_runsummary.py [min] [max]")
        print("       python send_runsummary.py (-> send all ridf files)")

    def set_worksheet(self) -> None:
        json_array = glob.glob(self.__work_dir + "send_runsummary/json/*.json")
        os.environ["GSPREAD_SILENCE_WARNINGS"] = "1"
        gc = gspread.service_account(filename=json_array[0])
        sh = gc.open(self.__spread_name)
        self.__ws = sh.sheet1

    def send_info(self) -> None:
        ridf_array = glob.glob(self.__path_data + "*.ridf")
        for i in range(len(ridf_array)):
            ridfname = ridf_array[i]
            runnum = int(ridfname[-9:-5])
            if self.__all or self.__run_min <= runnum <= self.__run_max:
                print("sending information: " + ridfname)
                self.send_single(ridfname)
                time.sleep(1)

    def send_single(self, ridfname: str) -> None:
        # size
        cmd = "ls -lh " + ridfname
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        sizeinfo = proc.communicate()[0].decode("utf-8")
        sizeinfo = sizeinfo.strip("\n")
        sizeinfo_array = re.split(" ", sizeinfo)
        size = sizeinfo_array[4].strip()

        # ridf summary
        cmd = self.__path_prinfo + " " + ridfname
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        babinfo = proc.communicate()[0].decode("utf-8")
        babinfo = babinfo.strip("\n")
        babinfo_array = re.split(" : |\n", babinfo)

        runname = babinfo_array[1].strip()
        runnumber = babinfo_array[3].strip()
        start = babinfo_array[5].strip()
        stop = babinfo_array[7].strip()
        date = babinfo_array[9].strip()
        header = babinfo_array[11].strip()
        ender = babinfo_array[13].strip()

        ds = self.__ws.range(
            "B" + str(int(runnumber) + 1) + ":I" + str(int(runnumber) + 1)
        )
        ds[0].value = runname
        ds[1].value = runnumber
        ds[2].value = date
        ds[3].value = start
        ds[4].value = stop
        ds[5].value = header
        ds[6].value = ender
        ds[7].value = size

        self.__ws.update_cells(ds)


if __name__ == "__main__":
    print("main called")
