from flask import Flask, render_template, redirect, url_for
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from itsdangerous import URLSafeTimedSerializer
from flask_wtf.csrf import CsrfProtect
from flask.ext.cors import CORS

app = Flask(__name__, )

app.config.from_object('config')

# everything that needs an initialization

lm = LoginManager()
lm.init_app(app)

lm.session_protection = "basic" # or strong depending on your needs
login_serializer = URLSafeTimedSerializer(app.secret_key)

csrf = CsrfProtect()
csrf.init_app(app)

db = SQLAlchemy(app)
CORS(app)


# Error Handlers for whole app

@app.errorhandler(400)
def bad_request(error):
    """Handle 400 errors."""
    return render_template("error/400.html"), 400


@app.errorhandler(401)
def not_authorized(error):
    """Handle 401 errors."""
    return render_template("error/401.html"), 401


@app.errorhandler(403)
def forbidden(error):
    """Handle 403 errors."""
    return render_template("error/403.html"), 403


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return render_template("error/404.html"), 404

@app.errorhandler(405)
def method_not_allowed(error):
    """Handle 405 errors."""
    return render_template("error/405.html", method=request.method), 405

    
# Importing views 
from app.auth.controller import auth
from app.admin.controller import admin
# register blueprints
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(admin, url_prefix='/admin')

@app.route('/')
def index():
    return redirect(url_for('auth.login'))
    
@app.errorhandler(500)
def internal_server_error(error):
    """Handle 500 errors."""
    return render_template("error/500.html"), 500
# init database 
db.create_all()