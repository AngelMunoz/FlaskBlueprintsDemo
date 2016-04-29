from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

app = Flask(__name__, )

app.config.from_object('config')

lm = LoginManager()
lm.init_app(app)
db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404
    
from app.auth.views import auth
# from app.main.controllers import main
app.register_blueprint(auth, url_prefix='/auth')
# app.register_blueprint(main, url_prefix='/')

db.create_all()