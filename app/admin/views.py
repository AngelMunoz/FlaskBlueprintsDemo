from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
from flask.ext.login import login_required, login_user, \
                            current_user, logout_user
# from sqlalchemy.exc import IntegrityError
from app import db, lm
# from app.admin.forms import # Admin forms
from app.models import User, Company, Subsidiary, Employee

admin = Blueprint('admin', __name__)

@admin.route('/home/')
@login_required
def home():
    return render_template('admin/home.html', title="Home")
    
@admin.route('/subsidiaries/')
@login_required
def subsidiaries():
    # render subsidiary template
    pass
@admin.route('/company/')
def company():
    # render company template
    pass
    
@admin.route('/employees/')
@login_required
def employees():
    # render employee template
    pass