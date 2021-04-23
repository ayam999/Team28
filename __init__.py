from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY']='thisissirstflaskapp'
app.config['SQLALCHMY_DATABASE_URI']='sqlite:///database/cjflask.db'
db=SQLAlchemy(app)
from codejana_flask import routes





