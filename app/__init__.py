from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from itsdangerous import URLSafeTimedSerializer
from flask_wtf.csrf import CsrfProtect

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

# Error Handlers for whole app

@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404

@app.errorhandler(403)
def forbidden(error):
    return render_template("403.html"), 403

@app.errorhandler(500)
def internal_error(error):
    return render_template("500.html"), 500

# Importing views 
from app.auth.controller import auth
from app.admin.controller import admin
# register blueprints
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(admin, url_prefix='/admin')
# init database 
db.create_all()