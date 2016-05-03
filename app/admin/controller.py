from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, jsonify
from flask.ext.login import login_required, login_user, \
                            current_user, logout_user
from sqlalchemy.exc import IntegrityError
from app import db, lm
from app.admin.forms import NewSubsidiaryForm, EditCompanyForm, \
                            EditSubsidiaryForm, NewEmployeeForm, \
                            EditEmployeeForm
from app.models import User, Company, Subsidiary, Employee

admin = Blueprint('admin', __name__)

@admin.route('/home/')
@login_required
def home():
    return render_template('admin/home.html', title="Home")


    
@admin.route('/company/', methods=['GET', 'PUT'])
def company():
    editcompform = EditCompanyForm(request.form)
    current_company = Company.query.filter(Company.user_id == current_user.id).first_or_404()
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

    
@admin.route('/subsidiaries/', methods=['GET','POST'])
@login_required
def subsidiaries():
    newsubform = NewSubsidiaryForm(request.form)
    current_company = Company.query.filter(Company.user_id == current_user.id).first_or_404()
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
                            
@admin.route('/subsidiaries/<sub_name>', methods=['GET', 'PUT', 'DELETE'])
@login_required
def subsidiary(sub_name):
    # look for the subsidiary with sub_name
    current_sub = Subsidiary.query.filter(Subsidiary.name == sub_name).first_or_404()
    sub_employees = current_sub.employees
    edit_subform = EditSubsidiaryForm(request.form)
    if request.method == 'PUT':
        if edit_subform.validate():
            edited_form =  check_sub_changes(current_sub, edit_subform)
            db.session.add(edited_form)
            # try commit
            try:
                db.session.commit()
            except IntegrityError: # catch for IntegrityErrr
                db.session.rollback()
                mess = "Either Name or the Interior number exist in the database"
                # return a success response
                return jsonify({"error":mess}), 409
        else:
            # return errors
            return jsonify(edit_subform.errors), 400
    if request.method == "DELETE":
        db.session.delete(current_sub)
        db.session.commit()
    return render_template("admin/subsidiary_detail.html",
                            editform=edit_subform,
                            subsidiary=current_sub,
                            title=current_sub.name,
                            employees=current_sub.employees)
    

    
    
@admin.route('/employees/', methods=['GET','POST'])
@login_required
def employees():
    current_company = Company.query.filter(Company.user_id == current_user.id).first_or_404()
    # send subsidiary item
    subsidiaries = current_company.subsidiaries
    # send new employee form
    newempform = NewEmployeeForm(request.form)
    sub_choices = [ (c.id, c.name) for c in Subsidiary.query.\
                    filter(Subsidiary.company_id == current_company.id).\
                    order_by(Subsidiary.name).all()]  
    newempform.subsidiary_id.choices = sub_choices
    if request.method == "POST":
        # validate form
        if newempform.validate():
            new_emp = Employee(newempform.email.data, newempform.password.data)
            if new_emp:
                new_emp.name = newempform.name.data
                new_emp.lastname = newempform.lastname.data
                if new_emp.second_name is not None:
                    new_emp.second_name = newempform.second_name.data
                new_emp.lastname = newempform.lastname.data
                if new_emp.second_lastname is not None:
                    new_emp.second_lastname = newempform.second_lastname.data 
                new_emp.rfc = newempform.rfc.data
                new_emp.job_name = newempform.job_name.data
                new_emp.subsidiary_id = newempform.subsidiary_id.data
                # add new employee
                db.session.add(new_emp)
                try:
                    # commit new employee to database
                    db.session.commit()
                except IntegrityError:
                    db.session.rollback()
                    mess = "Either Email or the RFC exist in the database"
                    return jsonify({"error":mess}), 400                
        else:
            return jsonify(newempform.errors), 400
    return render_template('admin/employee.html',
                            newempform=newempform,
                            current_company=current_company,
                            subsidiaries=subsidiaries)
    # navigate from employee to employee
    
    
@admin.route('/employees/<rfc>', methods=['GET','PUT','DELETE'])
@login_required
def employee(rfc):
    # look for the subsidiary with sub_name
    employee = Employee.query.filter(Employee.rfc == rfc).first_or_404()
    current_sub = Subsidiary.query.filter(Subsidiary.id == employee.subsidiary_id).first_or_404()
    edit_empform = EditEmployeeForm(request.form)
    current_company = Company.query.filter(Company.user_id == current_user.id).first_or_404()
    sub_choices = [ (c.id, c.name) for c in Subsidiary.query.\
                    filter(Subsidiary.company_id == current_company.id).\
                    order_by(Subsidiary.name).all()]  
    edit_empform.subsidiary_id.choices = sub_choices
    if request.method == 'PUT':
        if edit_empform.validate():
            edited_emp =  check_emp_changes(employee, edit_empform)
            db.session.add(edited_emp)
            # try commit
            try:
                db.session.commit()
            except IntegrityError: # catch for IntegrityErrr
                db.session.rollback()
                mess = "Either Name or the Interior number exist in the database"
                # return a success response
                return jsonify({"error":mess}), 409
        else:
            # return errors
            return jsonify(edit_subform.errors), 400
    if request.method == "DELETE":
        db.session.delete(employee)
        db.session.commit()
    return render_template("admin/employee_detail.html",
                            newempform=edit_empform,
                            current_sub=current_sub,
                            title=employee.name,
                            employee=employee,
                            company=current_company)


def check_sub_changes(subsidiary, form):
    edited_sub = subsidiary
    if subsidiary.name != form.name.data and form.name.data is not None:
        if len(form.name.data) > 1:
            edited_sub.name = form.name.data
    else:
        edited_sub.name = subsidiary.name
    if subsidiary.street != form.street.data and form.street.data is not None:
        if len(form.street.data) > 1:
            edited_sub.street = form.street.data
    else:
        edited_sub.street = subsidiary.street
    if subsidiary.suburb != form.suburb.data and form.suburb.data is not None:
        if len(form.suburb.data) > 1:
            edited_sub.suburb = form.suburb.data
    else:
        edited_sub.suburb = subsidiary.suburb
    if subsidiary.ext_number != form.ext_number.data \
       and form.ext_number.data is not None:
        edited_sub.ext_number = form.ext_number.data
    else:
        edited_sub.ext_number = subsidiary.ext_number
    if subsidiary.interior_number != form.interior_number.data \
       and form.interior_number.data is not None:
        edited_sub.interior_number = form.interior_number.data
    else:
        edited_sub.interior_number = subsidiary.interior_number
    if subsidiary.postal_code != form.postal_code.data \
       and form.postal_code.data is not None:
        edited_sub.postal_code = form.postal_code.data
    else:
        edited_sub.postal_code = subsidiary.postal_code
    if subsidiary.city != form.city.data and form.city.data is not None:
        if len(form.city.data) > 1:
            edited_sub.city = form.city.data
    else:
        edited_sub.city = subsidiary.city
    if subsidiary.country != form.country.data and form.country.data is not None:
        if len(form.country.data) > 1:
            edited_sub.country = form.country.data
    else:
        edited_sub.country = subsidiary.country
    
    return edited_sub
    
def check_emp_changes(employee,form):
    edited_emp = employee
    if employee.name != form.name.data and form.name.data is not None:
        if len(form.name.data) > 1:
            edited_emp.name = form.name.data
    else:
        edited_emp.name = employee.name
    if employee.email != form.email.data and form.email.data is not None:
        if len(form.email.data) > 1:
            edited_emp.email = form.email.data
    else:
        edited_emp.email = employee.email
    if employee.pw_hash != form.password.data and form.password.data is not None:
        if len(form.password.data) > 1:
            edited_emp.pw_hash = form.password.data
    else:
        edited_emp.pw_hash = employee.pw_hash
    if employee.second_name != form.second_name.data \
       and form.second_name.data is not None:
        if len(form.second_name.data) > 1:
            edited_emp.second_name = form.second_name.data
    else:
        edited_emp.second_name = employee.second_name
    if employee.lastname != form.lastname.data \
       and form.lastname.data is not None:
        if len(form.lastname.data) > 1:
            edited_emp.lastname = form.lastname.data
    else:
        edited_emp.lastname = employee.lastname
    if employee.second_lastname != form.second_lastname.data \
       and form.second_lastname.data is not None:
        if len(form.second_lastname.data) > 1:
            edited_emp.second_lastname = form.second_lastname.data
    else:
        edited_emp.second_lastname = employee.second_lastname
    if employee.rfc != form.rfc.data and form.rfc.data is not None:
        if len(form.rfc.data) > 1:
            edited_emp.rfc = form.rfc.data
    else:
        edited_emp.rfc = employee.rfc
    if employee.job_name != form.job_name.data and form.job_name.data is not None:
        if len(form.job_name.data) > 1:
            edited_emp.job_name = form.job_name.data
    else:
        edited_emp.job_name = employee.job_name
    if employee.subsidiary_id != form.subsidiary_id.data and form.subsidiary_id.data is not None:
        edited_emp.subsidiary_id = form.subsidiary_id.data
    else:
        edited_emp.subsidiary_id = employee.subsidiary_id
        
    return edited_emp