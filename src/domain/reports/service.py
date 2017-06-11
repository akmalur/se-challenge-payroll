# src/domain/reports/service.py
import calendar
import csv

import datetime

from decimal import Decimal
from flask_login import current_user

from src.domain.reports.report import Report
from src.domain.reports.reported_hours import ReportedHours


class ReportsService(object):
    def __init__(self, repository):
        self.repository = repository

    def createReport(self,
                     employee_id,
                     employer_id,
                     date,
                     amount_paid):

        monthrange = calendar.monthrange(date.year, date.month)
        if date.day <= 15:
            start_date = datetime.date(year=date.year, month=date.month, day=1)
            end_date = datetime.date(year=date.year, month=date.month, day=15)
        else:
            start_date = datetime.date(year=date.year, month=date.month, day=16)
            end_date = datetime.date(year=date.year, month=date.month, day=monthrange[1])

        report = Report(employee_id,
                        employer_id,
                        start_date,
                        end_date,
                        amount_paid)
        return report

    def getReportByID(self, report_id):
        doc = self.repository.get_by_id(report_id)
        return Report(**doc)

    def findByEmployerID(self, employer_id):
        docs = self.repository.find_by_employer_id(employer_id)
        return [Report(**doc) for doc in docs]

    def processReport(self, raw_data):
        reader = csv.reader(raw_data)
        hours = []
        report_id = None
        for row in reader:
            if reader.line_num == 1 or row == None or row == []:
                continue
            elif row[0] == 'report id':
                report_id = row[1]
            else:
                raw_date = row[0].split('/')
                date = datetime.date(day=int(raw_date[0]), month=int(raw_date[1]), year=int(raw_date[2]))
                hours.append(ReportedHours(employee_id=row[2],
                                           date=date,
                                           hours=Decimal(row[1]),
                                           job_group=row[3]))

        processedReport = self.repository.find_reportedHours(report_id)
        if processedReport != None:
            raise ImportError('Report already processed')

        for reportedHours in hours:
            reportedHours.report_id = report_id
            self.repository.save_hours(reportedHours.json())

        self.generatePayrollReport(hours)

    def generatePayrollReport(self, hours):
        for hour in hours:
            if hour.job_group == 'A':
                amount_paid = 20 * hour.hours
            else:
                amount_paid = 30 * hour.hours
            new_report = self.createReport(hour.employee_id, current_user.id, hour.date, amount_paid)
            existing_report = self.repository.find(new_report)
            if existing_report == None:
                self.repository.save_report(new_report.json())
            else:
                existing_report = Report(**existing_report)
                existing_report.amount_paid = existing_report.amount_paid + new_report.amount_paid
                existing_report.version += 1
                self.repository.update_report(existing_report)

