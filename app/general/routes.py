from datetime import datetime 
from flask import render_template, flash, redirect, url_for, request, current_app, jsonify
from app.general.forms import PostForm
from app.general import bp 


@bp.route("/", methods=["GET"])
@bp.route("/index", methods=["GET"])
@bp.route("/home", methods=["GET"])
def index():
    return render_template("page-new.html")