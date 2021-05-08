from flask import  Flask,render_template,session,redirect,url_for
from wtforms import StringField, PasswordField , SubmitField , RadioField,TextAreaField
from flask_wtf import FlaskForm
from  wtforms.validators import  DataRequired,Length,EqualTo, Email
from flask_wtf import FlaskForm
import json_loads





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

class update_sprint(FlaskForm):
    
    def update_sprint(self, id, name=None, startDate=None, endDate=None, state=None):
        payload = {}
        if name:
            payload["name"] = name
        if startDate:
            payload["startDate"] = startDate
        if endDate:
            payload["endDate"] = endDate
        if state:
            if (
                self._options["agile_rest_path"]
                == GreenHopperResource.GREENHOPPER_REST_PATH
            ):
                raise NotImplementedError(
                    "Public Jira API does not support state update"
                )
            payload["state"] = state

        url = self._get_url("sprint/%s" % id, base=self.AGILE_BASE_URL)
        r = self._session.put(url, data=json.db(payload))

    return json_loads(r)