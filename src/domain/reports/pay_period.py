# src/domain/reports/pay_period.py

class PayPeriod(object):
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def __str__(self):
        start_date_str = self.start_date.strftime("%d-%m-%y")
        end_date_str = self.end_date.strftime("%d-%m-%y")
        return '{} - {}'.format(start_date_str, end_date_str)

    def __repr__(self):
        return 'Pay Period: {}'.format(str(self))

    def json(self):
        return {
            'start_date': self.start_date,
            'end_date': self.end_date
        }