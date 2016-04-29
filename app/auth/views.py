from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash
from flask.ext.login import login_required, logout_user, current_user
from app import db, lm
from app.auth.forms import LoginForm, RegisterForm
from app.models import User

# Define the blueprint: 'auth', set its url prefix: app.url/auth`
auth = Blueprint('auth', __name__)

@auth.route('/signup/', methods=['GET', 'POST'])
def signup():
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        user = User(form.email.data, form.password.data)
        if user:
             # register user
             flash("You Signed Up successfuly" % user.name)
             return redirect(url_for("auth.login"))
        flash("Something went wrong, please try again.", 'error-message')
    return render_template("auth/signup.html", form=form)
    
    
@auth.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            user.authenticated = True
            db.session.add(user)
            db.session.commit()
            login_user(user, remember=True)
            flash("Welcome %s" % user.name)
            return redirect(url_for("auth.login"))
        flash("Wrong email or password", 'error-message')
    return render_template("auth/login.html", form=form)

@auth.route('/logout/', methods=['GET', 'POST'])
def logout():
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    return render_template("logout.html")

@lm.user_loader
def user_loader(mail):
    user = User.query.filter_by(email=mail).first()
    return user

@lm.request_loader
def request_loader(request):
    email = request.form.get('email')
    user = User.query.filter_by(email=mail).first()
    return user
    
@lm.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'
    
@auth.before_request
def before_request():
    g.user = current_user