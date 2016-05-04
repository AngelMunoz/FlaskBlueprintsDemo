import os
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL'] # pulling from enviromental variable,
                                                     # you could just hardcode the url string too.
# DATABASE_CONNECT_OPTIONS = {} # options for the database engine

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
