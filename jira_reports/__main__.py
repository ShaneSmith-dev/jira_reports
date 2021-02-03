"""
Starting attempt at making python utility to create JIRA reports
"""

# TODO: Group these based on category? User input, etc.
import getpass # Used to allow user to enter in password
import os.path # Used to get the user's home directory
import urllib3 # Used to disable warning 
import datetime # Used to get current date
from jira import JIRA # Python library to interface with JIRA REST api
from collections import Counter # Used to count dictionary items 
import argparse # Used to parse input arguments

from .config import load_config
from .timeframe import report_dates

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) # ignore warning about not doing certificate check

if __name__ == "__main__":
    current_date = datetime.date.today()
    parser = argparse.ArgumentParser()
    # TODO: Use groups to simplify logic here
    daterange = parser.add_mutually_exclusive_group()
    daterange.add_argument(
        "-current-week",
        action = "store_true",
        help = """Builds a report based on the current week.""",
    )
    daterange.add_argument(
        "-last-week",
        action = "store_true",
        help = """Builds a report based on last week.""",
    )
    daterange.add_argument(
        "-current-month",
        action = "store_true",
        help = """Builds a report based on the current month.""",
    )
    daterange.add_argument(
        "-last-month",
        action = "store_true",
        help = """Builds a report based on last month.""",
    )
    daterange.add_argument(
        "-current-year",
        action = "store_true",
        help = """Builds a report based on the current year.""",
    )
    daterange.add_argument(
        "-last-year",
        action = "store_true",
        help = """Builds a report based on last year.""",
    )
    report_type = parser.add_mutually_exclusive_group()
    report_type.add_argument(
        "-worklogs",
        action = "store_true",
        help = """Looks at work logged by the user(s) in the provided timeframe.""",
    )
    report_type.add_argument(
        "-resolved",
        action = "store_true",
        help = """Looks at issues resolved by the user(s) in the provided timeframe.""",
    )

    args = parser.parse_args()
    print(vars(args))
    report_times = report_dates(args,current_date)
    print(report_times)

    # Load configurations from file
    config = load_config()

    # Grab creds from user
    username = getpass.getuser()
    password = getpass.getpass("Jira password: ")

    # try:
    #     jira_handle = JIRA(
    #         options={"verify": False},
    #         server=config['server']['base_uri'],
    #         basic_auth=[username,password],
    #         max_retries=1
    #     )
    # except:
    #     print("Jira connection unsuccessful.")
