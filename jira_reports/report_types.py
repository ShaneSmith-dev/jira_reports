"""
This file is intended to house the classes used to help define the different report types.
"""

"""
Work logged in range of dates by specific users
worklogDate >= "afterDate" AND worklogDate <= "beforeDate" AND worklogAuthor in (userList)

Tasks completed in range of dates by specific users
resolved >= "afterDate" AND resolved <= "beforeDate" AND resolution changed BY (userList) 
"""

class ReportType():
    def __init__(self,time_range,user_list,report_type,filter_fields):
        self.time_range = time_range
        self.user_list = user_list
        self.report_type = report_type
        self.filter_fields = filter_fields

    def jql_query(self):
        if self.report_type == "worklogs":
            return("worklogDate >= " + self.time_range[0] + " AND worklogDate <= " + self.time_range[1] + " AND worklogAuthor in " + self.user_list)
        elif self.report_type == "resolved":
            return("resolved >= " + self.time_range[0] + " AND worklogDate <= " + self.time_range[1] + " AND worklogAuthor in " + self.user_list)
        else:
            return("Oops, unsupported report type selected")