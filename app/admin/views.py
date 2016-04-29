from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash
from flask.ext.login import login_required, login_user, \
                            current_user, logout_user
# from sqlalchemy.exc import IntegrityError
from app import db, lm
# from app.admin.forms import # Admin forms
from app.models import User, Company, Subsidiary, Employee

admin = Blueprint('auth', __name__)

@admin.route('/home/')
@login_required
def home():
    # render template of home
    pass
    
@admin.route('/subsidiaries/<subsidiary>')
@login_required
def subsidiary(subsidiary):
    # render subsidiary template
    pass
    
    
@admin.route('/employees/<rfc>')
@login_required
def employee(rfc):
    # render employee template
    pass