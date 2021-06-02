<<<<<<< HEAD

=======
<<<<<<< HEAD
from flask import Flask,render_template,request,flash,session,redirect,url_for,abort
from forms import LoginForm,SignOutForm,signupForm,addDemandForm
=======
<<<<<<< Updated upstream
>>>>>>> 5cd98cf5c04ea75deb75cad097c646e16a94a607
from flask import Flask, render_template, request, flash, session, redirect, url_for, abort
from forms import LoginForm, SignOutForm, signupForm, addDemandForm

from flask import Flask,render_template,request,flash,session,redirect,url_for,abort
from forms import LoginForm,SignOutForm,signupForm,addDemandForm
<<<<<<< HEAD

=======
>>>>>>> Stashed changes
>>>>>>> 722eda7077a4bbe418ac74ed9a1cbc8eab0dee39
>>>>>>> 5cd98cf5c04ea75deb75cad097c646e16a94a607
import pyrebase
import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials
from firebase_admin import firestore
app = Flask(__name__)

<<<<<<< HEAD
app.config['SECRET_KEY']='khawla'
import json 
=======
app = Flask(_name_)
app.config['SECRET_KEY'] = 'khawla'
import json
>>>>>>> 722eda7077a4bbe418ac74ed9a1cbc8eab0dee39
import os
import tempfile
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config['SECRET_KEY']='khawla'




#For Firebase JS SDK v7.20.0 and later, measurementId is optional
print(firebase_admin)
config={
  "apiKey": "AIzaSyDj83l21N_0vFiJP2_RhiUTN2qr8X84dfI" ,
  "authDomain": "flaskdb-fb78d.firebaseapp.com",
  "databaseURL": "https://flaskdb-fb78d-default-rtdb.firebaseio.com",
  "projectId": "flaskdb-fb78d",
  "storageBucket": "flaskdb-fb78d.appspot.com",
  "messagingSenderId": "291466022293",
  "appId": "1:291466022293:web:462cf3b91963df70b87a9c",
  "measurementId": "G-W08M46DJ3R"
}




cred = credentials.Certificate('flaskdb-fb78d-firebase-adminsdk-zmw6u-d4c4493a84.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

firebase = pyrebase.initialize_app(config)
auth= firebase.auth()
storage=firebase.storage()

@app.route('/devolper')
def developer():
    return redirect(url_for('developerPage'))

@app.route('/developerPage')
def developerPage():
    return render_template('developer.html')

@app.route('/admin')
def admin():
    return redirect(url_for('adminPage'))

@app.route('/adminPage')
def adminPage():
    return render_template('admin.html')

@app.route('/registerAdmin')
def registerAdmin():
    return redirect(url_for('registerAdmin'))

@app.route('/registerAdminPage')
def registerAdminPage():
    return render_template('registerAdmin.html')

@app.route('/scrumMaster')
def scrumMaster():
    return redirect(url_for('scrumMasterPage'))

@app.route('/scrumMasterPage')
def scrumMasterPage():
    return render_template('scrumMaster.html')


'''
@app.route('/')
@app.route('/login',methods=['GET', 'POST'])
def login():
    print("login")
    form = LoginForm()
    if request.method == 'POST':
    #if form.validate_on_submit():
        print("click")
        try:
            user=auth.sign_in_with_email_and_password(form.email.data,form.password.data)
            uid=auth.get_account_info(user['idToken'])['users'][0]['localId']
            session["uid"]=uid
            print("1")
            #uid={'email':form.email.data,'password':form.password.data}
            doc_ref=db.collection(u"Adminetabel").document(uid)
            doc = doc_ref.get()
            print(doc)
            if doc.exists:
                admin=doc.to_dict()['admin']
                print(admin)
                if(admin):
                    print("if a")
                    session["admin"]=True
                    session["user"]=form.email.data
                    #return redirect(url_for("adminPage"),form=form)
                    return render_template('admin.html',form=form)
                else:
                    print("els a")
                    session["admin"]=False
                    session["user"]=form.email.data
                    return redirect(url_for("developerPage"),form=form)
        except:
            return render_template('register.html',form=form,us="Not Exist")
    else:
        if "user" in session:
            print("111")
            if(session["admin"]):
                print("222")
                return redirect(url_for("adminPage"),form=form)
            else:
                return redirect(url_for("developerPage"),form=form)
        print("gggggg")
        return render_template('login.html',form=form)
'''





@app.route('/')
@app.route('/HomePage',methods=['GET', 'POST'])
def home():
    form = LoginForm()
    if form.validate_on_submit():
        try:
            auth.sign_in_with_email_and_password(form.email.data,form.password.data)
            session["userdeveloper"]=form.email.data
            return redirect(url_for("userdeveloper"))
        except:
            return render_template('login.html',form=form,us="Not Exist")
    else:
        if "userdeveloper" in session:
            return redirect(url_for("userdeveloper"))
        return render_template('login.html',form=form)


@app.route('/loginScrum',methods=['GET', 'POST'])
def loginScrumMaster():
    form = LoginForm()
    if form.validate_on_submit():
        try:
            auth.sign_in_with_email_and_password(form.email.data,form.password.data)
            session["userScrumMaster"]=form.email.data
            return redirect(url_for("userScrumMaster"))
        except:
            return render_template('loginScrumMaster.html',form=form,us="Not Exist")
    else:
        if "userScrumMaster" in session:
            return redirect(url_for("userScrumMaster"))
        return render_template('loginScrumMaster.html',form=form)

@app.route('/loginAdmine',methods=['GET', 'POST'])
def loginAdmine():
    form = LoginForm()
    if form.validate_on_submit():
        try:
            auth.sign_in_with_email_and_password(form.email.data,form.password.data)
            session["userAdmin"]=form.email.data
            return redirect(url_for("userAdmin"))
        except:
            return render_template('loginScrumMaster.html',form=form,us="Not Exist")
    else:
        if "userAdmin" in session:
            return redirect(url_for("userAdmin"))
        return render_template('loginAdmin.html',form=form)




@app.route('/userScrumMaster',methods=['GET', 'POST'])
def userScrumMaster():
    form = SignOutForm()
    if form.validate_on_submit():
        return redirect(url_for("logout"))
    return render_template('scrumMaster.html',form=form)

@app.route('/userdeveloper',methods=['GET', 'POST'])
def userdeveloper():
    form = SignOutForm()
    if form.validate_on_submit():
        return redirect(url_for("logout"))
    return render_template('developer.html',form=form)

@app.route('/userAdmin',methods=['GET', 'POST'])
def userAdmin():
    form = SignOutForm()
    if form.validate_on_submit():
        return redirect(url_for("logout"))
<<<<<<< HEAD

=======
<<<<<<< HEAD
    return render_template('admin.html',form=form)

=======
<<<<<<< Updated upstream
>>>>>>> 5cd98cf5c04ea75deb75cad097c646e16a94a607
    return render_template('admin.html', form=form)



    return render_template('admin.html',form=form)

>>>>>>> 722eda7077a4bbe418ac74ed9a1cbc8eab0dee39
@app.route('/userDemand',methods=['GET', 'POST'])
def userDemand():
    form = addDemandForm()
    if form.validate_on_submit():
        return redirect(url_for("logout"))
    return render_template('developer.html',form=form)
<<<<<<< HEAD

=======
<<<<<<< HEAD
=======
>>>>>>> Stashed changes
>>>>>>> 722eda7077a4bbe418ac74ed9a1cbc8eab0dee39
>>>>>>> 5cd98cf5c04ea75deb75cad097c646e16a94a607
'''
@app.route('/user',methods=['GET', 'POST'])
def user():
    form = SignOutForm()
    if form.validate_on_submit():
        return redirect(url_for("logout"))
    return render_template('login.html',form=form)
'''
@app.route('/logout')
def logout():
    session.pop("userdeveloper",None)
    return redirect(url_for("home"))
    



@app.route('/register',methods=['GET', 'POST'])
def register():
    form=signupForm()
    if request.method == 'POST':
        email=form.email.data
        password=form.password.data
        id=form.id.data
        firstname=form.firstname.data
        lastname=form.lastname.data
        try: 
            Developertabel=auth.create_user_with_email_and_password(email,password)
            data={"email":email,"password":password,"id":id,"firstname":firstname,"lastname":lastname}
            db.collection(u'Developertabel').document().set({"email":email,"password":password,"id":id,"firstname":firstname,"lastname":lastname})
            print(auth.get_account_info(userdeveloper['idToken'])['Developertabel'][0]['localId'])
            info=auth.get_account_info(userdeveloper['idToken'])['Developertabel'][0]['localId']
            db.collection(u'Developertabel').document(info).set(data)
            return redirect(url_for("developerPage"),form=form)
           # return render_template('developer.html',form=form)
        except:
            print("email already exist")
<<<<<<< HEAD

=======
<<<<<<< HEAD
    return render_template('register.html',form=form)
    
=======
<<<<<<< Updated upstream
>>>>>>> 5cd98cf5c04ea75deb75cad097c646e16a94a607
    return render_template('register.html', form=form)

    return render_template('register.html',form=form)


>>>>>>> 722eda7077a4bbe418ac74ed9a1cbc8eab0dee39

@app.route('/registerScrumMaster',methods=['GET', 'POST'])
def registerScrumMaster():
    form=signupForm()
    if request.method == 'POST':
        email=form.email.data
        password=form.password.data
        id=form.id.data
        firstname=form.firstname.data
        lastname=form.lastname.data
        try: 
            Developertabel=auth.create_user_with_email_and_password(email,password)
            data={"email":email,"password":password,"id":id,"firstname":firstname,"lastname":lastname}
            db.collection(u'ScrumMastertabel').document().set({"email":email,"password":password,"id":id,"firstname":firstname,"lastname":lastname})
            print(auth.get_account_info(userregisterScrumMaster['idToken'])['ScrumMastertabel'][0]['localId'])
            info=auth.get_account_info(userdeveloper['idToken'])['ScrumMastertabell'][0]['localId']
            db.collection(u'ScrumMastertabel').document(info).set(data)
            return redirect(url_for("scrumMasterPage"),form=form)
            #return render_template('scrumMaster.html',form=form)
        except:
            print("email already exist")
    return render_template('registerScrumMaster.html',form=form)


@app.route('/registerAdmine',methods=['GET', 'POST'])
def registerAdmine():
    form=signupForm()
    if request.method == 'POST':
        email=form.email.data
        password=form.password.data
        id=form.id.data
        firstname=form.firstname.data
        lastname=form.lastname.data
        try: 
            Developertabel=auth.create_user_with_email_and_password(email,password)
            data={"email":email,"password":password,"id":id,"firstname":firstname,"lastname":lastname}
            db.collection(u'Adminetabel').document().set({"email":email,"password":password,"id":id,"firstname":firstname,"lastname":lastname})
            print(auth.get_account_info(userregisterScrumMaster['idToken'])['Adminetabel'][0]['localId'])
            info=auth.get_account_info(userdeveloper['idToken'])['Adminetabel'][0]['localId']
            db.collection(u'Adminetabel').document(info).set(data)
            return redirect(url_for("adminPage"),form=form)
           # return render_template('scrumMaster.html',form=form)
        except:
            print("email already exist")
            #return redirect(url_for("registerAdminPage"),form=form)

    return render_template('registerAdmin.html',form=form)





<<<<<<< HEAD

=======
@app.route('/updetdeveloper/<post_id>/<text>/update',methods=['GET', 'POST'])
def updateDeveloper(post_id,text):
    form=updateComment()
    if form.validate_on_submit():
        data={'text':form.comment.data}
        db.collection(u'Comments').document(post_id).update(data)
        return redirect(url_for('parks'))
<<<<<<< HEAD
    return render_template('updateComment.html',form=form,admin=session["admin"],text=text)


=======
<<<<<<< Updated upstream
    return render_template('updateComment.html', form=form, admin=session["admin"], text=text)
=======
    return render_template('updateComment.html',form=form,admin=session["admin"],text=text)
>>>>>>> 5cd98cf5c04ea75deb75cad097c646e16a94a607






>>>>>>> 722eda7077a4bbe418ac74ed9a1cbc8eab0dee39
@app.route('/addDemand',methods=['GET', 'POST'])
def addDemand():
    form=addDemandForm()
    if request.method == 'POST':
        email=form.email.data
        demand=form.demand.data
        siprintNumber=form.dsiprintNumber.data
        try: 
<<<<<<< HEAD
           Demandabel=auth.create_user_with_email_and_password(email,demand,siprintNumbe)
           data={"email":email,"demand":demand,"siprintNumber":siprintNumber}
           db.collection(u'Demandtabel').document().set({"email":email,"demand":demand,"siprintNumber":siprintNumber})
           print(auth.get_account_info(userdemand['idToken'])['demandtabel'][0]['localId'])
           info=auth.get_account_info(userdemand['idToken'])['demandtabel'][0]['localId']
           db.collection(u'demandtabel').document(info).set(data)
           return redirect(url_for("addDemand"),form=form)
           # return render_template('developer.html',form=form)
        except:
            print("deman already exist")
=======
            Developertabel=auth.create_user_with_email_and_password(email,password)
            data={"email":email,"demand":demand,"siprintNumber":siprintNumber}
<<<<<<< HEAD
            db.collection(u'demandtabel').document().set({"email":email,"demand":demand,"siprintNumber":siprintNumber})
=======
            db.collection(u'Developertabel').document().set({"email":email,"demand":demand,"siprintNumber":siprintNumber})
>>>>>>> 722eda7077a4bbe418ac74ed9a1cbc8eab0dee39
            print(auth.get_account_info(userdemand['idToken'])['demandtabel'][0]['localId'])
            info=auth.get_account_info(userdeveloper['idToken'])['demandtabel'][0]['localId']
            db.collection(u'demandtabel').document(info).set(data)
            return redirect(url_for("addDemand"),form=form)
           # return render_template('developer.html',form=form)
        except:
<<<<<<< HEAD
            print("UserStory already exist")
    return render_template('addDemand.html',form=form)  

=======
            print("email already exist")
>>>>>>> 5cd98cf5c04ea75deb75cad097c646e16a94a607
    return render_template('addDemand.html',form=form)


   








<<<<<<< HEAD

=======
>>>>>>> Stashed changes
>>>>>>> 722eda7077a4bbe418ac74ed9a1cbc8eab0dee39
>>>>>>> 5cd98cf5c04ea75deb75cad097c646e16a94a607


if __name__ == '__main__':
    app.run(debug=True)
