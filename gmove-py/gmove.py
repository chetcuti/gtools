#!/usr/bin/env python3
"""
Author: Greg Chetcuti <greg@greg.ca>
Date: 2021-08-13
Purpose: Move the contents of one folder to another
"""

import configparser
import pathlib
import shutil

config = configparser.ConfigParser()
config.read(str(pathlib.Path(__file__).absolute())[:-2] + "ini")

source_dir = config["config"]["source_dir"]
target_dir = config["config"]["target_dir"]


# =============================================================================
# Main                                                                     Main
# ----------------------------------------------------------
def main():
    """Run the main program"""
    for item in pathlib.Path(source_dir).iterdir():
        shutil.move(str(pathlib.Path(source_dir / item)), str(target_dir))


# ----------------------------------------------------------
if __name__ == "__main__":
    main()

