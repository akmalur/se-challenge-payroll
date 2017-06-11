# src/web/reports/__init__.py

from flask import Blueprint

reports = Blueprint('reports', __name__)

from . import views
