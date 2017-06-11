# src/domain/reports/reported_hours.py

class ReportedHours(object):
    def __init__(self, employee_id, date, hours, job_group, report_id=None, id=None):
        self.id = id
        self.employee_id = employee_id
        self.date = date
        self.hours = hours
        self.job_group = job_group
        self.report_id = report_id

    def __repr__(self):
        result = 'Employee ID: {}, Date: {}, Hours: {}, Group: {}, Report ID: {}'
        return result.format(self.employee_id,
                             self.date,
                             self.hours,
                             self.job_group,
                             self.report_id)

    def json(self):
        return {
            'id': self.id,
            'employee_id': self.employee_id,
            'date': self.date,
            'hours': self.hours,
            'job_group': self.job_group,
            'report_id': self.report_id,
        }