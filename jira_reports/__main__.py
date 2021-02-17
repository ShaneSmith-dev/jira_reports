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
from .report_types import ReportType

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) # ignore warning about not doing certificate check

if __name__ == "__main__":
    current_date = datetime.date.today()
    parser = argparse.ArgumentParser()
    # TODO: Use groups to simplify logic here
    parser.add_argument(
        "-date-range",
        choices = ['current_week','last_week',
        'current_month','last_month',
        'current_year','last_year'],
        help = """Builds a report based on the time range entered.""",
    )
    parser.add_argument(
        "-report-type",
        choices = ['worklogs','resolved'],
        help = """Looks at work logged by the user(s) in the provided timeframe.""",
    )

    args = parser.parse_args()
    report_times = report_dates(args.date_range,current_date)

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
