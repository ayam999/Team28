<<<<<<< HEAD

from flask import  Flask,render_template,session,redirect,url_for
from wtforms import StringField, PasswordField , SubmitField , RadioField,TextAreaField
from flask_wtf import FlaskForm
from  wtforms.validators import  DataRequired,Length,EqualTo, Email

class  RigistrationForm(FlaskForm):
     username=StringField(label='username',validators=[DataRequired(),Length(min=3,max=20)])
     password=PasswordField(label='password',validators=[DataRequired(),Length(min=6,max=8)])
     id=StringField(label='id',validators=[DataRequired(),Length(min=9,max=9)])
     email=StringField(label='email',validators=[DataRequired(),Email()])
     firstname=StringField(label='firstname',validators=[DataRequired(),Length(min=3,max=20)])
     lastname=StringField(label='lastname',validators=[DataRequired(),Length(min=3,max=20)])
     comfirmPassward=PasswordField(label='comfirm Passward',validators=[DataRequired(),EqualTo('passwors')])
     submit=SubmitField(label='Sign up')



class LoginForm(FlaskForm):
    username = StringField(label='username', validators=[DataRequired(), Length(min=3, max=20)])
    password = PasswordField(label='password', validators=[DataRequired(), Length(min=6, max=8)])
=======
<<<<<<< Updated upstream
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
<<<<<<< HEAD
    submit = SubmitField('Login')

class SignOutForm(FlaskForm):
    submit = SubmitField('logout')

class addDemandForm(FlaskForm):
    email=StringField(label='email',validators=[DataRequired(),Email()])
    demand = TextAreaField(label='demand',validators=[DataRequired()])
    siprintNumber=StringField(label='siprintNumber',validators=[DataRequired(),Length(min=1,max=20)])
    submit = SubmitField('add')


=======
>>>>>>> 5cd98cf5c04ea75deb75cad097c646e16a94a607
    submit = SubmitField('Login')

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



class SignOutForm(FlaskForm):
    submit = SubmitField('logout')

class LoginForm(FlaskForm):
    email=StringField(label='email',validators=[DataRequired(),Email()])
    password = PasswordField(label='password', validators=[DataRequired(), Length(min=6, max=8)])
    submit = SubmitField('Login')

class addDemandForm(FlaskForm):
    email=StringField(label='email',validators=[DataRequired(),Email()])
    demand = StringField(label='demand',validators=[DataRequired(),Length(min=3,max=100)])
    siprintNumber=StringField(label='siprintNumber',validators=[DataRequired(),Length(min=1,max=20)])
    submit = SubmitField('add')

<<<<<<< HEAD

=======
>>>>>>> Stashed changes
>>>>>>> 722eda7077a4bbe418ac74ed9a1cbc8eab0dee39
>>>>>>> 5cd98cf5c04ea75deb75cad097c646e16a94a607
