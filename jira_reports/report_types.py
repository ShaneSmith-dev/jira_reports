"""
This file is intended to house the classes used to help define the different report types.
"""

class ReportType():
    def __init__(self,time_range,user_list,filter_fields):
        self.time_range = time_range
        self.user_list = user_list
        self.filter_fields = filter_fields

    def printQuery(self):
        return [self.time_range, self.user_list, self.filter_fields]