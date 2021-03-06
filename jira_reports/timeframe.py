"""
Based on current time and report type returns start and end dates for report.
"""

import datetime # Used to work with dates and times
from datetime import timedelta # Used to adjust dates as needed
import calendar # Used to (easily) find the number of days in each month

"""
Datetime Weekday Returns:
0 = Monday
1 = Tuesday
2 = Wednesday
3 = Thursday
4 = Friday
5 = Saturday
6 = Sunday
"""

start_of_year = datetime.date(2020,1,1)
end_of_year = datetime.date(2020,12,31)

def report_dates(date_range,current_date):
    curr_year = current_date.year
    curr_month = current_date.month

    if date_range == "current_week":
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
    elif date_range == "last_week":
        # We want to look at last week
        date_adj = timedelta(days=7)
        last_date = current_date - date_adj
        if last_date.weekday() == 0:
            afterDate = last_date.isoformat()
        else:
            date_adj = timedelta(days=last_date.weekday())
            adj_date = last_date - date_adj
            afterDate = adj_date.isoformat()
        date_adj = timedelta(days=6-last_date.weekday())
        adj_date = last_date + date_adj
        beforeDate = adj_date.isoformat()
    elif date_range == "current_month":
        # We want to look at the current month
        beforeDate = current_date.replace(day=calendar.monthrange(curr_year,curr_month)[1]).isoformat()
        afterDate = current_date.replace(day=1).isoformat()
    elif date_range == "last_month":
        # We want to look at last month
        month_adj = curr_month - 1
        year_adj = curr_year
        if (month_adj < 1):
            month_adj = 12
            year_adj = curr_year - 1
        beforeDate = current_date.replace(year=year_adj,month=month_adj,day=calendar.monthrange(curr_year,month_adj)[1]).isoformat()
        afterDate = current_date.replace(year=year_adj,month=month_adj,day=1).isoformat()
    elif date_range == "current_year":
        # We want to look at the current year
        beforeDate = end_of_year.replace(year=curr_year).isoformat()
        afterDate = start_of_year.replace(year=curr_year).isoformat()
    elif date_range == "last_year":
        # We want to look at last year
        beforeDate = end_of_year.replace(year=curr_year-1).isoformat()
        afterDate = start_of_year.replace(year=curr_year-1).isoformat()
    else:
        # We return just the current date, shouldn't get here TODO: Return error message instead?
        beforeDate = current_date.isoformat()
        afterDate = current_date.isoformat()
    return [afterDate, beforeDate]