"""
Starting attempt at making python utility to create JIRA reports
"""

# TODO: Group these based on category? User input, etc.
import getpass # Used to allow user to enter in password
import os.path # Used to get the user's home directory
import urllib3 # Used to disable warning 
from jira import JIRA # Python library to interface with JIRA REST api
from collections import Counter # Used to count dictionary items 
import argparse # Used to parse input arguments
import toml # Used to parse config file(s)
import time # Not sure if I need this one
import datetime # Used to work with dates and times
from datetime import timedelta # Used to adjust dates as needed

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

    # Load configurations from file TODO: Create intialization function if it doesn't exist
    home_dir = os.path.expanduser("~")
    config_path = os.path.join(home_dir,"AppData","Local","jira_reports","jira_reports_config.toml")
    config = toml.load(config_path)

    # Grab creds from user
    username = getpass.getuser()
    password = getpass.getpass("Jira password: ")
