from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, jsonify
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
    
@admin.route('/subsidiaries/', methods=['GET','POST'])
@login_required
def subsidiaries():
    newsubform = NewSubsidiaryForm(request.form)
    if request.method == "POST": 
        if newsubform.validate():
            # validate this form
            print('valid new sub')
            # remember you need to add the company's id to the sub
            # before adding it to the database
        else:
            return jsonify(newsubform.errors), 400
    
@admin.route('/company/', methods=['GET', 'PUT'])
def company():
    editcompform = EditCompanyForm(request.form)
    current_company = Company.query.filter(User.id == current_user.id).first()
    if request.method == "PUT":
        if editcompform.validate():
            # validate this form
            print('edit valid')
        else:
            return jsonify(editcompform.errors), 400             
    return render_template("admin/company.html", newsubform=newsubform,
                            editcompform=editcompform,
                            subsidiaries=subsidiaries,
                            company=current_company)
    
    
@admin.route('/employees/')
@login_required
def employees():
    # render employee template
    pass