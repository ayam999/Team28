#from App import Demand
from flask import  Flask,render_template,session,redirect,url_for
from wtforms import StringField, PasswordField , SubmitField , RadioField,TextAreaField
from flask_wtf import FlaskForm
from  wtforms.validators import  DataRequired,Length,EqualTo, Email
from flask_wtf import FlaskForm




class signupForm(FlaskForm):
     email=StringField(label='email',validators=[DataRequired(),Email()])
     password=PasswordField(label='password',validators=[DataRequired(),Length(min=6,max=8)])
     id=StringField(label='id',validators=[DataRequired(),Length(min=9,max=9)])
     firstname=StringField(label='firstname',validators=[DataRequired(),Length(min=3,max=20)])
     lastname=StringField(label='lastname',validators=[DataRequired(),Length(min=3,max=20)])
     submit=SubmitField(label='Sign up')




class LoginForm(FlaskForm):
    email=StringField(label='email',validators=[DataRequired(),Email()])
    password = PasswordField(label='password', validators=[DataRequired(), Length(min=6, max=8)])
    submit = SubmitField('Login')

class SignOutForm(FlaskForm):
    submit = SubmitField('logout')
'''
class addDemandForm(FlaskForm):
    email=StringField(label='email',validators=[DataRequired(),Email()])
    password=PasswordField(label='email',validators=[DataRequired(),Email()])
    demand = TextAreaField(label='demand',validators=[DataRequired()])
    siprintNumber=StringField(label='siprintNumber',validators=[DataRequired(),Length(min=1,max=20)])
    submit = SubmitField('add')
    '''

class addDemandForm(FlaskForm):
    email = StringField("email", validators=[DataRequired()])
    Demand= StringField("Demand", validators=[DataRequired()])
    #demandNumber= StringField("demandNumber", validators=[DataRequired()])
    submit = SubmitField('add demand')


class DeleteDemanForm(FlaskForm):
    email = StringField("email", validators=[DataRequired()])

    Demand = StringField("Demand", validators=[DataRequired()])
    submit = SubmitField('Delete Deman')

class DeleteDeveloperForm(FlaskForm):
    email = StringField("email", validators=[DataRequired()])
    submit = SubmitField('Delete Developer')  