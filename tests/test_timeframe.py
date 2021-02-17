"""
Test for timeframe.py
"""

import datetime
from jira_reports.timeframe import report_dates

birth_date = datetime.date(1974,8,14)
freeze_date = datetime.date(1999,12,31)
start_of_year = datetime.date(2021,1,1)
# TODO: Add short month
# TODO: Add leapyear

def test_report_dates():
    # "Normal" Day
    case1 = report_dates("current_week", birth_date)
    assert case1[0] == "1974-08-12"
    assert case1[1] == "1974-08-18"
    case2 = report_dates("last_week", birth_date)
    assert case2[0] == "1974-08-05"
    assert case2[1] == "1974-08-11"
    case3 = report_dates("current_month", birth_date)
    assert case3[0] == "1974-08-01"
    assert case3[1] == "1974-08-31"
    case4 = report_dates("last_month", birth_date)
    assert case4[0] == "1974-07-01"
    assert case4[1] == "1974-07-31"
    case5 = report_dates("current_year", birth_date)
    assert case5[0] == "1974-01-01"
    assert case5[1] == "1974-12-31"
    case6 = report_dates("last_year", birth_date)
    assert case6[0] == "1973-01-01"
    assert case6[1] == "1973-12-31"

    # End of Year
    case7 = report_dates("current_week", freeze_date)
    assert case7[0] == "1999-12-27"
    assert case7[1] == "2000-01-02"
    case8 = report_dates("last_week", freeze_date)
    assert case8[0] == "1999-12-20"
    assert case8[1] == "1999-12-26"
    case9 = report_dates("current_month", freeze_date)
    assert case9[0] == "1999-12-01"
    assert case9[1] == "1999-12-31"
    case10 = report_dates("last_month", freeze_date)
    assert case10[0] == "1999-11-01"
    assert case10[1] == "1999-11-30"
    case11 = report_dates("current_year", freeze_date)
    assert case11[0] == "1999-01-01"
    assert case11[1] == "1999-12-31"
    case12 = report_dates("last_year", freeze_date)
    assert case12[0] == "1998-01-01"
    assert case12[1] == "1998-12-31"

    # Start of Year
    case13 = report_dates("current_week", start_of_year)
    assert case13[0] == "2020-12-28"
    assert case13[1] == "2021-01-03"
    case14 = report_dates("last_week", start_of_year)
    assert case14[0] == "2020-12-21"
    assert case14[1] == "2020-12-27"
    case15 = report_dates("current_month", start_of_year)
    assert case15[0] == "2021-01-01"
    assert case15[1] == "2021-01-31"
    case16 = report_dates("last_month", start_of_year)
    assert case16[0] == "2020-12-01"
    assert case16[1] == "2020-12-31"
    case17 = report_dates("current_year", start_of_year)
    assert case17[0] == "2021-01-01"
    assert case17[1] == "2021-12-31"
    case18 = report_dates("last_year", start_of_year)
    assert case18[0] == "2020-01-01"
    assert case18[1] == "2020-12-31"