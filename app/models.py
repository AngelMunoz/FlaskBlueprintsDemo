from app import db


class User(db.Model):
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
    authenticated = db.Column(db.Boolean, default=False)
    companies       = db.relationship('Company', uselist=False, back_populates="users")
    
    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)
    
    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.email

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False
    
    
    
    def __init__(self, email, password):
        self.mail = mail
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
    user_id         = db.Column(db.Integer, db.ForeignKey('user.id'),
                                                       nullable=False)
    user            = db.relationship("users", back_populates='User.companies')
    subsidiaries    = db.relationship('Subsidiary')
    
    def __init__(self, name, user_id):
        self.name = name
        self.user = user
    
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
    
    def __init__(self, name, street, suburb, ext_number, interior_number,
                 postal_code, city, country, company_id):
        self.name
        self.street
        self.suburb
        self.ext_number
        self.interior_number
        self.postal_code
        self.city
        self.country
        self.company_id
    
class Employee(db.Model):
    """
    Model representing the Employee
    """
    __tablename__ = 'employees'
    id              = db.Column(db.Integer, primary_key=True)
    email           = db.Column(db.String(128), nullable=False,
                                              unique=True)
    password        = db.Column(db.String(192), nullable=False)
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
                                            
    def __init__(self, name, email, password, lastname, second_lastname, rfc, job_name,
                 subsidiary_id):
        self.name = name
        self.mail = mail
        self.password = password
        self.lastname = lastname
        self.second_lastname = second_lastname
        self.rfc = rfc 
        self.job_name = job_name
        self.subsidiary_id = subsidiary_id