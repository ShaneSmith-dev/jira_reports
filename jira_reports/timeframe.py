"""
Based on current time and report type returns start and end dates for report.
"""

import datetime # Used to work with dates and times
from datetime import timedelta # Used to adjust dates as needed

def report_dates(input_args):
    # Grab current date
    current_date = datetime.date.today()

    if input_args.current_week:
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
    else:
        beforeDate = current_date.isoformat()
        afterDate = current_date.isoformat()
    return [afterDate, beforeDate]