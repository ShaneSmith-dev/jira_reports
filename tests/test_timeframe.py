"""
Test for timeframe.py
"""

from jira_reports.timeframe import report_dates

birth_date = "1974-08-14"
freeze_date = "1999-12-31"
start_of_year = "2021-01-01"

def test_report_dates():
    curr_week = {"current_week": True, "last_week": False,
    "current_month": False, "last_month": False,
    "current_year": False, "last_year": False,
    }
    case1 = report_dates(curr_week, birth_date)