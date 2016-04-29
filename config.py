DEBUG = True

import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:admin123@127.0.0.1/examen_timbox_db'
DATABASE_CONNECT_OPTIONS = {}

# App threads, a common assumption is
# using 2 per available processor cores to handle
# incoming requests using one and performing background 
# tasks with the other
THREADS_PER_PAGE = 2

# Enable protection against *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# sign the data with a special secure key
CSRF_SESSION_KEY = 'SOME SECRET KEY'

# secret key for cookies
SECRET_KEY = "SOME SECRET KEY FOR COOKIES"