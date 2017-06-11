# src/web/reports/views.py

from flask import render_template, flash, url_for, redirect
from flask_login import login_required, current_user

from . import reports as rp
from src.common.database import Database
from src.domain.reports import createReportsService
from src.web.reports.upload_report import UploadReportForm

reportsService = createReportsService(Database)


def report_view_model(report):
    return {
        'Employee ID': report.employee_id,
        'Pay Period': str(report.pay_period),
        'Amount Paid': '${}'.format(report.amount_paid)
    }


@rp.route('/reports', methods=['GET', 'POST'])
@login_required
def reports():
    reports = [report_view_model(r) for r in reportsService.findByEmployerID(current_user.id)]
    return render_template('reports/reports.html', reports=reports, title="Reports")


@rp.route('/report', methods=['GET', 'POST'])
@login_required
def upload_report():
    form = UploadReportForm()
    if (form.validate_on_submit()):
        file = form.file.data.read().decode("utf-8").split('\n')
        try:
            reportsService.processReport(file)
            flash('Report processed successfully!')
        except ImportError:
            flash('This report was previously processed.')
        return redirect(url_for('reports.reports'))


    return render_template('reports/report.html',
                           action="Upload",
                           form=form,
                           title="Upload Report")
