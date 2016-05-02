from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, jsonify
from flask.ext.login import login_required, login_user, \
                            current_user, logout_user
from sqlalchemy.exc import IntegrityError
from app import db, lm
from app.admin.forms import NewSubsidiaryForm, EditCompanyForm, \
                            EditSubsidiaryForm
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
    current_company = Company.query.filter(User.id == current_user.id).first_or_404()
    if request.method == "POST": 
        if newsubform.validate():
            new_sub = Subsidiary()
            new_sub.name = newsubform.name.data
            new_sub.street = newsubform.street.data
            new_sub.suburb = newsubform.suburb.data
            new_sub.ext_number = newsubform.ext_number.data
            new_sub.interior_number = newsubform.interior_number.data
            new_sub.postal_code = newsubform.postal_code.data
            new_sub.city = newsubform.city.data
            new_sub.country = newsubform.country.data
            new_sub.company_id = current_company.id
            db.session.add(new_sub)
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()
                mess = "Either Name or the Interior number exist in the database"
                return jsonify({"error":mess}), 409
        else:
            return jsonify(newsubform.errors), 400
    company_subs = current_company.subsidiaries
    return render_template("admin/subsidiary.html",
                            newsubform=newsubform,
                            subsidiaries=company_subs)
                            
@admin.route('/subsidiaries/<sub_name>', methods=['GET', 'PUT'])
@login_required
def subsidiary(sub_name):
    # look for the subsidiary with sub_name
    print("looking for %s" % sub_name)
    current_sub = Subsidiary.query.filter(Subsidiary.name == sub_name).first_or_404()
    sub_employees = current_sub.employees
    edit_subform = EditSubsidiaryForm(request.form)
    if request.method == 'PUT':
        if edit_subform.validate():
            edited_form =  check_sub_changes(current_sub, edit_subform)
            db.session.add(edited_form)
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()
                mess = "Either Name or the Interior number exist in the database"
                return jsonify({"error":mess}), 409
            # try commit
            # catch for IntegrityErrr
            # return a success response
            print('Form valid')
        else:
            # return errors
            return jsonify(edit_subform.errors), 400
    return render_template("admin/subsidiary_detail.html",
                            editform=edit_subform,
                            subsidiary=current_sub,
                            title=current_sub.name,
                            employees=current_sub.employees)
    
    
@admin.route('/company/', methods=['GET', 'PUT'])
def company():
    editcompform = EditCompanyForm(request.form)
    current_company = Company.query.filter(User.id == current_user.id).first_or_404()
    subsidiaries = current_company.subsidiaries
    if request.method == "PUT":
        if editcompform.validate():
            current_company.name = editcompform.new_name.data
            db.session.add(current_company)
            try:
                db.session.commit()
            except IntegrityError:
                mess = "That Name is Already Taken"
                return jsonify({"error":mess}), 409
        else:
            return jsonify(editcompform.errors), 400             
    return render_template("admin/company.html",
                            editform=editcompform,
                            company=current_company,
                            title=current_company.name,
                            subsidiaries=subsidiaries)
    
    
@admin.route('/employees/')
@login_required
def employees():
    # render employee template
    pass
    


def check_sub_changes(subsidiary, form):
    edited_sub = subsidiary
    if subsidiary.name == form.name.data \
       and len(form.name.data) > 1:
        edited_sub.name = form.name.data
    else:
        edited_sub.name = subsidiary.name
    if subsidiary.street == form.street.data \
       and len(form.street.data) > 1:
        edited_sub.street = form.street.data
    else:
        edited_sub.street = subsidiary.street
    if subsidiary.suburb == form.suburb.data \
       and len(form.suburb.data) > 1:
        edited_sub.suburb = form.suburb.data
    else:
        edited_sub.suburb = subsidiary.suburb
    if subsidiary.ext_number == form.ext_number.data \
       and len(form.extnumber.data) > 1:
        edited_sub.ext_number = form.ext_number.data
    else:
        edited_sub.ext_number = subsidiary.ext_number
    if subsidiary.interior_number == form.interior_number.data \
       and len(form.interior_number.data) > 1:
        edited_sub.interior_number = form.interior_number.data
    else:
        edited_sub.interior_number = subsidiary.interior_number
    if subsidiary.postal_code == form.postal_code.data \
       and len(form.postal_code.data) > 1:
        edited_sub.postal_code = form.postal_code.data
    else:
        edited_sub.postal_code = subsidiary.postal_code
    if subsidiary.city == form.city.data and len(form.city.data) > 1:
        edited_sub.city = form.city.data
    else:
        edited_sub.city = subsidiary.city
    if subsidiary.country == form.country.data \
       and len(form.country.data) > 1:
        edited_sub.country = form.country.data
    else:
        edited_sub.country = subsidiary.country
    
    return edited_sub