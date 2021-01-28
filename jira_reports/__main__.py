"""
Starting attempt at making python utility to create JIRA reports
"""

import getpass
import urllib3
from jira import JIRA
from collections import Counter
import argparse
import time
import datetime
from datetime import timedelta

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) # ignore warning about not doing certificate check

if __name__ == "__main__":
    current_date = datetime.date.today()
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-current-week",
        action = "store_true",
        default = False,
        help = """Builds a report based on the current week.""",
    )
    parser.add_argument(
        "-last-week",
        action = "store_true",
        default = False,
        help = """Builds a report based on last week.""",
    )
    parser.add_argument(
        "-current-month",
        action = "store_true",
        default = False,
        help = """Builds a report based on the current month.""",
    )
    parser.add_argument(
        "-last-month",
        action = "store_true",
        default = False,
        help = """Builds a report based on last month.""",
    )
    parser.add_argument(
        "-current-year",
        action = "store_true",
        default = False,
        help = """Builds a report based on the current year.""",
    )
    parser.add_argument(
        "-last-year",
        action = "store_true",
        default = False,
        help = """Builds a report based on last year.""",
    )

    args = parser.parse_args()

    # todo: pull this into its own function
    if args.current_week:
        # We want to look at the current week
        if current_date.weekday() == 0:
            afterDate = current_date.isoformat()
        else:
            date_adj = timedelta(days=current_date.weekday())
            adj_date = current_date - date_adj
            afterDate = adj_date.isoformat()
        date_adj = timedelta(days=6-current_date.weekday())
        adj_date = current_date + date_adj
        beforeDate = adj_date.isoformat()

    # Grab creds from user
    username = getpass.getuser()
    password = getpass.getpass("Jira password: ")
