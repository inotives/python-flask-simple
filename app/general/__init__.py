from flask import Blueprint

bp = Blueprint('main', __name__)

from app.general import routes
