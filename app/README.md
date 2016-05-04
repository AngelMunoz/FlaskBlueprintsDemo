# app
this directory contains specific settings and functionality about the application.

one of the main files is __init__.py where most of the initializations are made.
- admin contains Admin module specific code
- auth contain Authentication module specific code
- templates contains all the html jinja2 templates used in the application (the V in mvc)
- static contains all the client side stuff like libraries, client side code, etc.
- models.py contains the definitions for the database objects.


# Models

there are 4 basic models in this application
- User
- Company
- Subsidiary
- Employee

## User
For the user model we're also using this user for authentication so we use Flask-Login.
```python
from app import db
from flask.ext.login import UserMixin
class User(db.model, UserMixin):
    # everything inside the class, then:
    
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
```
what flask-login needs here is just the `is_active, is_authenticated, is_anonymous`
flask-login uses these properties to manage user session and cookies.
Also note that we're not storing the password in plain text, but rather the hash of the password.

```python
from app import db
from werkzeug import check_password_hash, generate_password_hash
from flask.ext.login import UserMixin

class User(db.Model, UserMixin):
    # everything inside the class, then:
    
     def set_password(self, password):
        self.pw_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)
```

because plain text passwords in a database are a bad idea, always assume your user's data will be compromised some day
and prepare accordingly.

*There

## Templates
Flask uses by default the templating engine called Jinja which takes an html file with some new syntax and parses it to plain html.
however you could also write your templates in jade too, with [PyJade](https://github.com/syrusakbary/pyjade) package for your flask application.
templates are a very simple thing to use, perhaps at the start they may look hard to read, but
you could always use a plugin in your text editor to enable highlighting.

I have three directories containing jinja2 templates:

- admin
- auth
- error

in each case there is a **base.html** file which as the name indicates, it is the base for the other
templates to inherit and focus more on the specific template instead having a single enormous html file to debug.

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        {% block head %}
        <!-- this is an html comment and this will be shown in the final html file -->
        {#
            this is a jinja comment and this will not be shown in the final html file
        #} 
        {% endblock %}
    </head>
    <body>
        {% block content %}
        {% endblock%}
        {% block scripts %}
        {% endblock %}
    </body>
</html>
```
this example is basically what a jinja template is it's just html with some new syntax in it
which will allow us to do more things in a individual way.
the `{% block content %}{% endblock %}` is telling the jinja engine where to pull more content from other file.

say we have file 2 and we want to show a view that has basically the same components as the first one
but you only want to change the central part.

```html
{% extends "admin/base.html" %} 
{# this will tell the jinja compiler that we will add stuff to base #}
{% block head %}
 {{ super() }} {# this will load that is in the head block in the parent template #}
{% endblock %}
{% block content %}
<p>this will be rendered inside block content using the structure inside base.html</p>
{% endblock%}
```
the final result will be
```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <!-- this is an html comment and this will be shown in the final html file -->
    </head>
    <body>
        <p>this will be rendered inside block content using the structure inside base.html</p>
    </body>
</html>
```
that's what jinja does with our templates (our views).
for each module please visit its readme file for further explanations.