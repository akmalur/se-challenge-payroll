# src/domain/reports/report.py
from src.domain.reports.pay_period import PayPeriod


class Report(object):
    def __init__(self, employee_id, employer_id, start_date, end_date, amount_paid, version=1, id=None):
        self.id = id
        self.employee_id = employee_id
        self.employer_id = employer_id
        self.pay_period = PayPeriod(start_date, end_date)
        self.amount_paid = amount_paid
        self.version = version

    def __repr__(self):
        result = 'Employee ID: {}, Pay Period: {}, Amount Paid: {}'
        return result.format(self.employee_id, str(self.pay_period), self.amount_paid)

    def json(self):
        return {
            'id': self.id,
            'employee_id': self.employee_id,
            'employer_id': self.employer_id,
            'start_date': self.pay_period.start_date,
            'end_date': self.pay_period.end_date,
            'amount_paid': self.amount_paid,
            'version': self.version
        }