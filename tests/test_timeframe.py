"""
Test for timeframe.py
"""

import datetime
from jira_reports.timeframe import report_dates

birth_date = datetime.date(1974,8,14)
freeze_date = datetime.date(1999,12,31)
start_of_year = datetime.date(2021,1,1)

class testArgs():
    def __init__(self,cw,lw,cm,lm,cy,ly):
        self.current_week = cw
        self.last_week = lw
        self.current_month = cm
        self.last_month = lm
        self.current_year = cy
        self.last_year = ly

curr_week = testArgs(True,False,False,False,False,False)
last_week = testArgs(False,True,False,False,False,False)
curr_month = testArgs(False,False,True,False,False,False)
last_month = testArgs(False,False,False,True,False,False)
curr_year = testArgs(False,False,False,False,True,False)
last_year = testArgs(False,False,False,False,False,True)

def test_report_dates():
    case1 = report_dates(curr_week, birth_date)
    assert case1[0] == "1974-08-12"
    assert case1[1] == "1974-08-18"
    case2 = report_dates(last_week, birth_date)
    assert case2[0] == "1974-08-05"
    assert case2[1] == "1974-08-11"
    case3 = report_dates(curr_month, birth_date)
    assert case3[0] == "1974-08-01"
    assert case3[1] == "1974-08-31"