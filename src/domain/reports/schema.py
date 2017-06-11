# src/domain/reports/schema
from sqlalchemy import Integer, Numeric, Column, Date, ForeignKey, String

from src.common.database import Database


class ReportSchema(Database.MODEL):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True)
    employer_id = Column(Integer, ForeignKey('users.id'))
    employee_id = Column(Integer, index=True)
    start_date = Column(Date, index=True)
    end_date = Column(Date, index=True)
    amount_paid = Column(Numeric(8, 2))
    version = Column(Integer)

    def json(self):
        return {
            'id': self.id,
            'employer_id': self.employer_id,
            'employee_id': self.employee_id,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'amount_paid': self.amount_paid,
            'version': self.version
        }

class ReportedHoursSchema(Database.MODEL):
    __tablename__ = "hours"

    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer)
    date = Column(Date)
    hours = Column(Numeric(4,2))
    job_group = Column(String)
    report_id = Column(Integer)

    def json(self):
        return {
            'id': self.id,
            'employee_id': self.employee_id,
            'date': self.date,
            'hours': self.hours,
            'job_group': self.job_group,
            'report_id': self.report_id
        }