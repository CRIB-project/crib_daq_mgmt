import sys
import os
import subprocess
import gspread
import time
import yaml
from pathlib import Path
from typing import Optional, Tuple


class Sender:
    def __init__(self, args: list[str]):
        self.__work_dir = Path(__file__).parent.parent
        self.__run_range = self.__parse_args(args)
        self.__config = self.__load_config()
        self.__worksheet = self.__init_worksheet()

    def __parse_args(self, args: list[str]) -> Tuple[Optional[int], Optional[int]]:
        """Parse command line arguments and return run range"""
        if len(args) == 1:
            return None, None  # All runs
        elif len(args) == 2:
            run_num = int(args[1])
            return run_num, run_num
        elif len(args) == 3:
            run_min = int(args[1])
            run_max = int(args[2])
            return min(run_min, run_max), max(run_min, run_max)
        else:
            self.__show_usage()
            sys.exit(1)

    def __load_config(self) -> dict:
        """Load configuration from YAML file"""
        config_path = self.__work_dir / "config.yaml"
        with open(config_path, "r", encoding="utf-8") as fin:
            config = yaml.safe_load(fin)
        return config

    def __init_worksheet(self) -> gspread.Worksheet:
        """Initialize Google Sheets worksheet"""
        json_path = next((self.__work_dir / "send_runsummary/json").glob("*.json"))
        os.environ["GSPREAD_SILENCE_WARNINGS"] = "1"
        gc = gspread.service_account(filename=str(json_path))
        sheet_name = self.__config["runsummary_config"]["sheetname"]
        return gc.open(sheet_name).sheet1

    def __show_usage(self) -> None:
        """Show usage information"""
        print("ERROR: input error or there are no such ridf file")
        print("USAGE: python send_runsummary.py [runnumber]")
        print("       python send_runsummary.py [min] [max]")
        print("       python send_runsummary.py (-> send all ridf files)")

    def __get_file_size(self, filepath: str) -> str:
        """Get readable file size"""
        cmd = f"ls -lh {filepath}"
        proc = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return proc.stdout.strip().split()[4]

    def __get_ridf_info(self, filepath: str) -> dict:
        """Get RIDF file information"""
        prinfo_path = self.__config["runsummary_config"]["prinfo"]
        cmd = f"{prinfo_path} {filepath}"
        proc = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        info = proc.stdout.strip().split(" : |\n")

        return {
            "runname": info[1].strip(),
            "runnumber": info[3].strip(),
            "start": info[5].strip(),
            "stop": info[7].strip(),
            "date": info[9].strip(),
            "header": info[11].strip(),
            "ender": info[13].strip(),
        }

    def __update_worksheet(self, run_info: dict, size: str) -> None:
        """Update worksheet with run information"""
        row = int(run_info["runnumber"]) + 1
        cell_range = f"B{row}:I{row}"
        cells = self.__worksheet.range(cell_range)

        values = [
            run_info["runname"],
            run_info["runnumber"],
            run_info["date"],
            run_info["start"],
            run_info["stop"],
            run_info["header"],
            run_info["ender"],
            size,
        ]

        for cell, value in zip(cells, values):
            cell.value = value

        self.__worksheet.update_cells(cells)

    def send_info(self) -> None:
        """Send information for all matching RIDF files"""
        ridf_path = self.__work_dir / "ridf"
        ridf_files = list(ridf_path.glob("*.ridf"))

        for ridf_file in ridf_files:
            run_num = int(ridf_file.stem[-4:])
            run_min, run_max = self.__run_range

            if (run_min is None and run_max is None) or (run_min <= run_num <= run_max):
                print(f"sending information: {ridf_file}")
                self.send_single(str(ridf_file))
                time.sleep(1)

    def send_single(self, ridf_path: str) -> None:
        """Send information for a single RIDF file"""
        size = self.__get_file_size(ridf_path)
        run_info = self.__get_ridf_info(ridf_path)
        self.__update_worksheet(run_info, size)


if __name__ == "__main__":
    print("main called")
