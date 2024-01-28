#!/usr/bin/env python3
"""
Author: Greg Chetcuti <greg@chetcuti.com>
Date: 2021-08-03
Purpose: CLI Randomizer
"""

import argparse
import configparser
import pathlib
from gjcode import rand as gjcr

config = configparser.ConfigParser()
config.read(str(pathlib.Path(__file__).absolute())[:-2] + "ini")

default_options = int(config["config"]["number_of_options"])
default_rolls = int(config["config"]["number_of_rolls"])
default_details = int(config["config"]["show_full_details"])


# =============================================================================
# Main                                                                     Main
# ----------------------------------------------------------
def main():
    """Run the main program"""
    args = get_args(default_options, default_rolls, default_details)

    if args.details == 1:
        print()
        print(gjcr.rand(args.options, args.rolls, 1))
        print()
    else:
        print(gjcr.rand(args.options, args.rolls, 0))


# =============================================================================
# Arguments                                                           Arguments
# ----------------------------------------------------------
def get_args(options, rolls, details):
    """Get the command-line arguments"""
    parser = argparse.ArgumentParser(
        description="CLI Randomizer",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-o",
        "--options",
        default=options,
        metavar="options",
        help="Number of options",
        type=int,
    )
    parser.add_argument(
        "-r",
        "--rolls",
        default=rolls,
        metavar="rolls",
        help="Number of rolls",
        type=int,
    )
    parser.add_argument(
        "-d",
        "--details",
        default=details,
        metavar="details",
        help="Show full details?",
        type=int,
    )
    args = parser.parse_args()

    if args.options == int(options) and args.rolls == int(rolls):
        print()
        user_input = input(
            "Random is going to run with "
            + f"{args.options}"
            + " options and "
            + f"{args.rolls:,}"
            + " rolls, is that ok? [y/N] "
        )
        if user_input in ["n", "N", ""]:
            print()
            parser.error("Defaults declined, and no CLI options specified")

    return args


# ----------------------------------------------------------
if __name__ == "__main__":
    main()

