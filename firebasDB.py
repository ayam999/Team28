from flask import Flask,render_template,request,flash,session,redirect,url_for,abort
from forms import LoginForm,SignOutForm
from flask_jsglue import JSGlue
import pyrebase
import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials
from firebase_admin import firestore
app = Flask(__name__)
jsglue = JSGlue(app)

import json 
import os
import tempfile
from werkzeug.utils import secure_filename


import firebase_admin
from firebase_admin import credentials


app.config['SECRET_KEY']='khwala'

cred = credentials.Certificate("flaskdb-fb78d-firebase-adminsdk-zmw6u-d4c4493a84.json")
firebase_admin.initialize_app(cred)



firebase = pyrebase.initialize_app(config)
auth= firebase.auth()
storage=firebase.storage()

# For Firebase JS SDK v7.20.0 and later, measurementId is optional
Config = {
  apiKey: "AIzaSyDj83l21N_0vFiJP2_RhiUTN2qr8X84dfI",
  authDomain: "flaskdb-fb78d.firebaseapp.com",
  databaseURL: "https://flaskdb-fb78d-default-rtdb.firebaseio.com",
  projectId: "flaskdb-fb78d",
  storageBucket: "flaskdb-fb78d.appspot.com",
  messagingSenderId: "291466022293",
  appId: "1:291466022293:web:462cf3b91963df70b87a9c",
  measurementId: "G-W08M46DJ3R"
}




db = firestore.client()

