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
    
@admin.route('/subsidiaries/')
@login_required
def subsidiaries():
    # render subsidiaries form
    pass
    
@admin.route('/company/', methods=['GET', 'POST'])
def company():
    newsubform = NewSubsidiaryForm()
    editcompform = EditCompanyForm()
    this_company="compa" # placeholder
    subsidiaries = [{'name':'s'},{'name':'g'},{'name':'h'}]
    if request.method == "POST":
        if "postal_code" in request.form: # Add a new Subsidiary case
            for key in request.form:
                if key in newsubform:
                    newsubform[key].data = request.form[key]    
            if newsubform.validate():
                # validate this form
                print('valid new sub')
                # remember you need to add the company's id to the sub
                # before adding it to the database
            else:
                return jsonify(newsubform.errors), 400
        else: # Edit Company's Name case
            for key in request.form:
                if key in editcompform:
                    editcompform[key].data = request.form[key]
            if editcompform.validate():
                # validate this form
                print('edit valid')
            else:
                return jsonify(editcompform.errors), 400            
            
    return render_template("admin/company.html", newsubform=newsubform,
                            editcompform=editcompform,
                            subsidiaries=subsidiaries,
                            company=this_company)
    
    
@admin.route('/employees/')
@login_required
def employees():
    # render employee template
    pass