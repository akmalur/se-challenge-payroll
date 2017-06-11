# src/domain/reports/repository
from src.domain.reports.schema import ReportSchema, ReportedHoursSchema


class ReportsRepository(object):
    def __init__(self, db):
        self.db = db

    def save_report(self, doc):
        session = self.db.SESSION()
        report = ReportSchema(**doc)

        try:
            session.add(report)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return doc

    def save_hours(self, doc):
        session = self.db.SESSION()
        hours = ReportedHoursSchema(**doc)

        try:
            session.add(hours)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return doc

    def find_reportedHours(self, report_id):
        session = self.db.SESSION()

        try:
            report = session.query(ReportedHoursSchema).filter_by(report_id=report_id).first()
        finally:
            session.close()

        return report


    def update_report(self, report):
        session = self.db.SESSION()

        try:
            doc = session.query(ReportSchema).filter_by(
                id=report.id,
                version=report.version-1
            ).first()
            if doc == None:
                raise LookupError("Version mismatch")
            doc.amount_paid = report.amount_paid
            doc.version = report.version
            session.add(doc)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

    def find(self, new_report):
        session = self.db.SESSION()

        try:
            report = session.query(ReportSchema).filter_by(
                employer_id=new_report.employer_id,
                employee_id=new_report.employee_id,
                start_date=new_report.pay_period.start_date
            ).first()
        finally:
            session.close()

        if report == None:
            return report
        else:
            return report.json()

    def get_by_id(self, id):
        session = self.db.SESSION()

        try:
            report = session.query(ReportSchema).filter(ReportSchema.id == id).first()
        finally:
            session.close()

        if report == None:
            return report
        else:
            return report.json()

    def find_by_employer_id(self, employer_id):
        session = self.db.SESSION()

        try:
            reports = session.query(ReportSchema).filter_by(employer_id=employer_id).order_by(ReportSchema.start_date.desc(), ReportSchema.employee_id).all()
        finally:
            session.close()
        if reports == None:
            return reports
        else:
            return [report.json() for report in reports]