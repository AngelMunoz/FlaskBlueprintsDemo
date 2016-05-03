from app import db
from werkzeug import check_password_hash, generate_password_hash
from flask.ext.login import UserMixin
class User(db.Model, UserMixin):
    """
    Model Representing the user.
    """
    __tablename__ = 'users'
    id              = db.Column(db.Integer, primary_key=True)
    email           = db.Column(db.String(128), nullable=False,
                                              unique=True)
    pw_hash         = db.Column(db.String(192), nullable=False)
    name            = db.Column(db.String(60), nullable=False)
    second_name     = db.Column(db.String(60))
    lastname        = db.Column(db.String(45), nullable=False)
    second_lastname        = db.Column(db.String(45), nullable=False)
    date_created    = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified   = db.Column(db.DateTime, default=db.func.current_timestamp(),
                                            onupdate=db.func.current_timestamp())
    rfc             = db.Column(db.String(45), nullable=False)
    authenticated   = db.Column(db.Boolean, default=False)
    company       = db.relationship('Company', uselist=False, backref="User")
    
    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)
    
    @property
    def is_active(self):
        """True, as all users are active."""
        return True
    @property
    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated
    @property
    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False
    
    
    
    def __init__(self, email, password):
        self.email = email
        self.set_password(password)
        
    def __repr__(self):
        return '<User %r>' % (self.name)


class Company(db.Model):
    """
    Model Representing the Company
    """
    __tablename__ = 'companies'
    id              = db.Column(db.Integer, primary_key=True)
    name            = db.Column(db.String(128), nullable=False)
    user_id         = db.Column(db.Integer, db.ForeignKey(User.id),
                                                       nullable=False)
    subsidiaries    = db.relationship('Subsidiary')
    
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return '<Company %r>' % (self.name)

class Subsidiary(db.Model):
    """
    Model representing the Subsidiary
    """
    __tablename__ = 'subsidiaries'
    id              = db.Column(db.Integer, primary_key=True)
    name            = db.Column(db.String(80), nullable=False)
    street          = db.Column(db.String(80), nullable=False)
    suburb          = db.Column(db.String(45), nullable=False)
    ext_number      = db.Column(db.Integer, nullable=False)
    interior_number = db.Column(db.Integer, nullable=False)
    postal_code     = db.Column(db.Integer, nullable=False)
    city            = db.Column(db.String(60), nullable=False)
    country         = db.Column(db.String(50), nullable=False)
    company_id      = db.Column(db.Integer, db.ForeignKey(Company.id),
                                            nullable=False)
    employees       = db.relationship('Employee')
    
    def __repr__(self):
        return '<Subsidiary %r, Parent Company Id: %r>' % (self.name, self.company_id)
    
class Employee(db.Model):
    """
    Model representing the Employee
    """
    __tablename__ = 'employees'
    id              = db.Column(db.Integer, primary_key=True)
    email           = db.Column(db.String(128), nullable=False,
                                              unique=True)
    pw_hash        = db.Column(db.String(192), nullable=False)
    name            = db.Column(db.String(60), nullable=False)
    second_name     = db.Column(db.String(60))
    lastname        = db.Column(db.String(45), nullable=False)
    second_lastname        = db.Column(db.String(45), nullable=False)
    date_created    = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified   = db.Column(db.DateTime, default=db.func.current_timestamp(),
                                            onupdate=db.func.current_timestamp())
    rfc             = db.Column(db.String(45), nullable=False)
    job_name        = db.Column(db.String(60), nullable=False)
    subsidiary_id   = db.Column(db.Integer, db.ForeignKey(Subsidiary.id),
                                            nullable=False)
                 
    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)
                                            
    def __init__(self, email, password):
        self.email = email
        self.set_password(password)