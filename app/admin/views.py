from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
from flask.ext.login import login_required, login_user, \
                            current_user, logout_user
from sqlalchemy.exc import IntegrityError
from app import db, lm
from app.admin.forms import NewSubsidiaryForm, EditCompanyForm
from app.models import User, Company, Subsidiary, Employee

admin = Blueprint('admin', __name__)

@admin.route('/home/')
@login_required
def home():
    return render_template('admin/home.html', title="Home")
    
@admin.route('/subsidiaries/<subsidiaryid>')
@login_required
def subsidiaries():
    # render subsidiaries form
    pass
@admin.route('/company/' methods=['GET', 'POST'])
def company():
    newsubform = NewSubsidiaryForm
    editcompform = EditCompanyForm
    if newsubform.validate_on_submit():
        # validate this form
        pass
    if editcompform.validate_on_submit():
        # validate this form
        pass
    return render_template("admin/company.html", newsubform=newsubform,
                            editcompform=editcompform,
                            subsidiaries=subsidiaries,
                            company=this_company)
    
    
@admin.route('/employees/')
@login_required
def employees():
    # render employee template
    pass