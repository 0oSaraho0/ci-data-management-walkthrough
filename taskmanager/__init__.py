
# this file will make sure to initalise our task manager applicaion as 
# a package allowing us to use our own
# imports as well as the standard ones

import os
import re
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env  # noqa


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL") # local
else:
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri # heroku

db = SQLAlchemy(app)

# the computer will complain this is not being imported at the top of the page
# with the other imports.  It is here because the route file will rel on using
# 'app and 'db' variables above.  if we try and import routes first we'll get
# a circular imports error because the variables have not been defined
# noqa stands for no quality assurance. we use this because what we have put in
# is correct but it is throwing an error.
from taskmanager import routes  # noqa