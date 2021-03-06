from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, jsonify
from werkzeug import check_password_hash, generate_password_hash
from flask_login import login_required, login_user, current_user, logout_user
from sqlalchemy.exc import IntegrityError
from app import db, lm
from app.auth.forms import LoginForm, RegisterForm
from app.models import User, Company
# Define the blueprint: 'auth', set its url prefix: app.url/auth
auth = Blueprint('auth', __name__)

@auth.route('/signup/', methods=['GET', 'POST'])
def signup():
    form = RegisterForm(request.form)
    if request.method == "POST":
        if form.validate():
            user = User(form.email.data, form.password.data)
            if user:
                user.name = form.name.data
                if user.second_name is not None:
                    user.second_name = form.second_name.data
                user.lastname = form.lastname.data
                if user.second_lastname is not None:
                    user.second_lastname = form.second_lastname.data 
                user.rfc = form.rfc.data
                # add company
                db.session.add(user)
                try:
                    db.session.commit()
                except IntegrityError:
                    db.session.rollback()
                    mess = "Either Email or the RFC exist in the database"
                    flash(mess)
                    return render_template("auth/signup.html", form=form, title="Sign Up")
                company = Company(form.company.data)
                company.user_id = user.id
                db.session.add(company)
                db.session.commit()
                flash("%s Signed Up successfuly with your Company %s" % (user.name, company.name))
                return redirect(url_for("auth.login"))
            flash("Something went wrong, please try again.", 'error-message')
        else:
            return jsonify(form.errors), 400
    return render_template("auth/signup.html", form=form, title="Sign Up")
    
    
@auth.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if g.user is not None and g.user.is_authenticated:
        print("User %s logged in" % g.user.name)
        return redirect(url_for('admin.home'))
    if request.method == "POST":
        if form.validate():
            user = User.query.filter_by(email=form.email.data).first()
            if user and check_password_hash(user.pw_hash, form.password.data):
                user.authenticated = True
                db.session.add(user)
                db.session.commit()
                login_user(user, remember=True)
                flash("Welcome %s" % user.name)
                return redirect(url_for("admin.home"))
            else:
                mess = "Wrong email or password"
                return jsonify({"error":mess}), 404
            flash("Wrong email or password", 'error-message')
        else:
            return jsonify(form.errors), 400
    return render_template("auth/login.html", form=form, title="Log in")

@auth.route('/logout/', methods=['GET', 'POST'])
@login_required
def logout():
    print(current_user)
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    return render_template("auth/logout.html", title="Log out")

@lm.user_loader
def user_loader(email):
    print("User loader")
    return User.query.get(email)
    
@auth.before_app_request
def load_user():
    g.user = current_user