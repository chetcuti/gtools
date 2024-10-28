#!/usr/bin/env python3
"""
Author: Greg Chetcuti <greg@greg.ca>
Date: 2021-08-03
Purpose: Send notifications from the CLI
"""

import argparse
import configparser
import pathlib
import socket
import requests

config = configparser.ConfigParser()
config.read(str(pathlib.Path(__file__).absolute())[:-2] + "ini")

api_url = config["config"]["api_url"]
api_key = config["config"]["api_key"]


# =============================================================================
# Main                                                                     Main
# ----------------------------------------------------------
def main():
    """Run the main program"""
    args = get_args()
    request_body = {
        "api_key": api_key,
        "subject": args.subject,
        "message": args.message,
        "url": args.url,
        "priority": args.priority,
    }
    requests.post(api_url, json=request_body)


# =============================================================================
# Arguments                                                           Arguments
# ----------------------------------------------------------
def get_args():
    """Get the command-line arguments"""
    parser = argparse.ArgumentParser(
        description="Send notifications from the CLI",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "subject",
        metavar="subject",
        help="Message subject",
        type=str,
    )
    parser.add_argument(
        "message",
        metavar="message",
        help="Message to send",
        type=str,
    )
    parser.add_argument(
        "-u",
        "--url",
        default="",
        help="URL",
        metavar="url",
        type=str,
    )
    parser.add_argument(
        "-p",
        "--priority",
        default=0,
        help="Priority",
        metavar="priority",
        type=int,
    )
    return parser.parse_args()


# ----------------------------------------------------------
if __name__ == "__main__":
    main()

