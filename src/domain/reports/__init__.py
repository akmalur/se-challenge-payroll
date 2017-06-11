# src/domain/reports/__init__.py

from .repository import ReportsRepository
from .service import ReportsService

def createReportsService(db):
    reports_repository = ReportsRepository(db)
    return ReportsService(reports_repository)