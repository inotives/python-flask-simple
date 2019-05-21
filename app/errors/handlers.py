from flask import render_template 
from app.errors import bp 

@bp.app_errorhandler(404)
def not_found_error(err):
    return render_template('errors/404.html'), 400

@bp.app_errorhandler(500)
def internal_error(err):
    return render_template('errors/500.html'), 500