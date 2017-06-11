# src/web/reports.py
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import DataRequired


class UploadReportForm(FlaskForm):
    file = FileField('Report', validators=[DataRequired()])
    submit = SubmitField('Submit')