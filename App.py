from flask import Flask,render_template,request,flash,session,redirect,url_for,abort
from forms import  DeleteSprintForm,addSprintForm,LoginForm,SignOutForm,signupForm,addDemandForm,DeleteDemanForm,DeleteDeveloperForm,UpdateDeveloperForm,DeleteScrumMasterForm,UpdateScrumMasterForm,UpdateSDemandForm,addProjectForm,DeleteProjectForm
import pyrebase
import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials
from firebase_admin import firestore
app = Flask(__name__)

app.config['SECRET_KEY']='khawla'
import json 
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

@app.route('/Demand')
def Demand():
    return redirect(url_for('addDemandPage'))

@app.route('/addDemandPage')
def addDemandPage():
    return render_template('addDemand.html')


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




@app.route('/userregisterScrumMaste',methods=['GET', 'POST'])
def userregisterScrumMaste():
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
    return render_template('admin.html',form=form)

@app.route('/userDemand',methods=['GET', 'POST'])
def userDemand():
    form = SignOutForm()
    if form.validate_on_submit():
        return redirect(url_for("logout"))
    return render_template('addDemand.html',form=form)
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
    return render_template('register.html',form=form)
    

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
            print(auth.get_account_info(userregisterScrumMaste['idToken'])['ScrumMastertabel'][0]['localId'])
            info=auth.get_account_info(userregisterScrumMaste['idToken'])['ScrumMastertabell'][0]['localId']
            db.collection(u'ScrumMastertabel').document(info).set(data)
            #return redirect(url_for("scrumMasterPage"),form=form)
            return render_template('scrumMaster.html',form=form)
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
            print(auth.get_account_info(userAdmin['idToken'])['Adminetabel'][0]['localId'])
            info=auth.get_account_info(userAdmin['idToken'])['Adminetabel'][0]['localId']
            db.collection(u'Adminetabel').document(info).set(data)
            return redirect(url_for("adminPage"),form=form)
           # return render_template('scrumMaster.html',form=form)
        except:
            print("email already exist")
            #return redirect(url_for("registerAdminPage"),form=form)

    return render_template('registerAdmin.html',form=form)



'''
@app.route('/addDemand',methods=['GET', 'POST'])
def addDemand():
    form=addDemandForm()
    if request.method == 'POST':
        email=form.email.data
        password=form.passwordl.data
        demand=form.demand.data
        sprintNumper=demand=form.sprintNumper.data
        demandNumber=form.demandNumber.data
        try: 
            Developertabel=auth.create_user_with_email_and_password(email,password)
            data={"email":email,"password":password,"demand":demand,"sprintNumper":sprintNumper,"demandNumber":demandNumber}
            db.collection(u'DemandTabel').document().set({"email":email,"password":password,"demand":demand,"sprintNumper":sprintNumper,"demandNumber":demandNumber})
            print(auth.get_account_info(userDemand['idToken'])['DemandTabel'][0]['localId'])
            info=auth.get_account_info(userDemand['idToken'])['DemandTabel'][0]['localId']
            db.collection(u'DemandTabel').document(info).set(data)
            return redirect(url_for("addDemandPage"),form=form)
           # return render_template('scrumMaster.html',form=form)
        except:
            print("demand already exist")
            #return redirect(url_for("registerAdminPage"),form=form)

    return render_template('registerAdmin.html',form=form)


'''


@app.route('/addDemand', methods =['GET','POST'])
def addDemand():
    form = addDemandForm()
    if form.validate_on_submit():
        data = {
        "name": form.email.data,
        "other": form.Demand.data,
        #"other": form.demandNumber.data,
        #" Demand": form. Demand.data,

        
        }
        docs = db.collection(u'DemandTabel').stream()
        canAddDemand = True
        for doc in docs:
            dici = doc.to_dict()
            #if data["name"] == dici['name'] and data["other"] == dici['other']and data["Demand"] == dici['Demand']:
            
            if data["name"] == dici['name'] and data["other"] == dici['other']:
                canAddDemand = False

        if canAddDemand:
            db.collection(u'DemandTabel').document().set(data)
            flash("add new Demand  ")
        else:
            flash(" Demand didint added ")

        return redirect(url_for('addDemand'))
    return render_template('addDemand.html', form=form)

@app.route('/deleteDeman', methods =['GET','POST'])
def deleteDeman():
    form = DeleteDemanForm()
    if form.validate_on_submit():

        req = request.form
        email = req["email"]
        Demand  = req["Demand"]

        docs = db.collection(u'DemandTabel').stream()
        for doc in docs:
            dici = doc.to_dict()
            if email == dici['name'] and Demand  == dici['other']:
                print (f"DemandTabel {dici['name']} in {dici['other']} has beem deleted")
                db.collection(u'DemandTabel').document(doc.id).delete()
                flash("Delete Deman")


        return redirect(url_for('deleteDeman'))
    return render_template('DeleteDeman.html', form=form)


@app.route('/deleteDeveloper', methods =['GET','POST'])
def deleteDeveloper():
    form = DeleteDeveloperForm()
    
    if form.validate_on_submit():

        req = request.form
        emailDeveloper = req["email"]
        
        docs=db.collection(u'Developertabel').stream()
        for doc in docs:
            dici = doc.to_dict()
            if emailDeveloper == dici['email']:
                print (f"Developer {dici['email']} in {dici['firstname']} has beem deleted")
                db.collection(u'Developertabel').document(doc.id).delete()
                flash("Developer has been deleted")
            else:
                print("this developer is not exits")
       

        return redirect(url_for('deleteDeveloper'))
    return render_template('deleteDeveloper.html', form=form,)


@app.route('/Developers/<string:email>/update', methods=['GET', 'POST'])
def UpdateDeveloper(email):
    print("into UpdateDeveloper")
    docs = db.collection(u'Developertabel').stream()
    canMakeDev = True
    for doc in docs:
        dici = doc.to_dict()
        if  dici['email']==email :
            canMakeDev = False
            rpost=dici['firstname']
            emailDev=dici['email']
            wanted=dici
    if canMakeDev:
        abort(403)
           
    else:
        rrpost=rpost
    ref_comment=db.collection(u'Developertabel')
    ref_my=ref_comment.where(u'email',u'==',email).stream()
    for r in ref_my:
        rr=r.to_dict()['email']
        print(rr)

    form = UpdateDeveloperForm()
    print(form.email.data)
    if form.validate_on_submit():
        print("after")
        email = form.email.data
        firstName = form.firstname.data
        id=form.id.data
        lastName = form.lastname.data
        password=form.password.data
        print(password)
        ref_comment=db.collection(u'Developertabel')
        ref_my=ref_comment.where(u'email',u'==',email).get()
        field_updates={"firstname":firstName,"lastname":lastName,"email":email,"id":id,"password":password}
        for r in ref_my:
            rr=ref_comment.document(r.id)
            rr.update(field_updates)
        
        flash('updating success', 'success')
        return redirect(url_for('UpdateDeveloper', email=emailDev))
    elif request.method == 'GET':
        print("get")
        docs
        form.email.data = wanted['email']
        form.firstname.data = wanted['firstname']
        form.id.data = wanted['id']
        form.lastname.data=wanted['lastname']
        form.password.data=wanted['password']
    return render_template('UpdateDeveloper.html', title='Update Developer',form=form, legend='Update Developer')


 
@app.route('/deleteScrumMaster', methods =['GET','POST'])
def deleteScrumMaster():
    form = DeleteScrumMasterForm()
    
    if form.validate_on_submit():

        req = request.form
        emailScrumMaster = req["email"]
        
        docs=db.collection(u'ScrumMastertabel').stream()
        for doc in docs:
            dici = doc.to_dict()
            if emailScrumMaster == dici['email']:
                print (f"ScrumMaster {dici['email']} in {dici['firstname']} has beem deleted")
                db.collection(u'ScrumMastertabel').document(doc.id).delete()
                flash("ScrumMaster has been deleted")
            else:
                print("this ScrumMaster is not exits")
       

        return redirect(url_for('deleteScrumMaster'))
    return render_template('deleteScrumMaster.html', form=form,)

@app.route('/ScrumMaster/<string:email>/update', methods=['GET', 'POST'])
def UpdateScrumMaster(email):
    print("into UpdateScrumMaster")
    docs = db.collection(u'ScrumMastertabel').stream()
    canMakeScrum = True
    for doc in docs:
        dici = doc.to_dict()
        if  dici['email']==email :
            canMakeScrum = False
            rpost=dici['firstname']
            emailScrum=dici['email']
            wanted=dici
    if canMakeScrum:
        abort(403)
           
    else:
        rrpost=rpost
    ref_comment=db.collection(u'ScrumMastertabel')
    ref_my=ref_comment.where(u'email',u'==',email).stream()
    for r in ref_my:
        rr=r.to_dict()['email']
        print(rr)

    form = UpdateScrumMasterForm()
    print(form.email.data)
    if form.validate_on_submit():
        print("after")
        email = form.email.data
        firstName = form.firstname.data
        id=form.id.data
        lastName = form.lastname.data
        password=form.password.data
        print(password)
        ref_comment=db.collection(u'ScrumMastertabel')
        ref_my=ref_comment.where(u'email',u'==',email).get()
        field_updates={"firstname":firstName,"lastname":lastName,"email":email,"id":id,"password":password}
        for r in ref_my:
            rr=ref_comment.document(r.id)
            rr.update(field_updates)
        
        flash('updating success', 'success')
        return redirect(url_for('UpdateScrumMaster', email=emailScrum))
    elif request.method == 'GET':
        print("get")
        docs
        form.email.data = wanted['email']
        form.firstname.data = wanted['firstname']
        form.id.data = wanted['id']
        form.lastname.data=wanted['lastname']
        form.password.data=wanted['password']
    return render_template('UpdateScrumMaster.html', title='Update ScrumMaster',form=form, legend='Update Developer')
    

    
@app.route('/Demand/<string:email>/update', methods=['GET', 'POST'])
def UpdateDemand(email):
    print("into Update Demands")
    docs = db.collection(u'DemandsTaple').stream()
    canMakeDemand = True
    for doc in docs:
        dici = doc.to_dict()
        if  dici['email']==email :
            canMakeDemand = False
            rpost=dici['demand']
            emailDemand=dici['email']
            status=dici['status']
            wanted=dici
    if canMakeDemand:
        abort(403)
           
    else:
        rrpost=rpost
    ref_comment=db.collection(u'DemandsTaple')
    ref_my=ref_comment.where(u'email',u'==',email).stream()
    for r in ref_my:
        rr=r.to_dict()['email']
        print(rr)

    form = UpdateSDemandForm()
    print(form.email.data)
    if form.validate_on_submit():
        print("after")
        email = form.email.data
        Demand = form.Demand.data
        status=form.status.data
        #print(password)
        ref_comment=db.collection(u'DemandsTaple')
        ref_my=ref_comment.where(u'email',u'==',email).get()
        field_updates={"email":email,"demand":Demand,"status":status}
        for r in ref_my:
            rr=ref_comment.document(r.id)
            rr.update(field_updates)
        
        flash('updating success', 'success')
        return redirect(url_for('UpdateDemand', email=emailDemand))
    elif request.method == 'GET':
        print("get")
        docs
        form.email.data = wanted['email']
        form.Demand.data = wanted['demand']
        form.status.data=wanted['status']
        
    return render_template('UpdateDemand.html', title='Update Demand',form=form, legend='Update Demand')


@app.route('/addProject', methods =['GET','POST'])
def addProject():
    form = addProjectForm()
    if form.validate_on_submit():
        data = {
        "name": form.email.data,
        "other": form.Project.data,
        #"other": form.demandNumber.data,
        #" Demand": form. Demand.data,

        
        }
        docs = db.collection(u'ProjectTabel').stream()
        canAddProject = True
        for doc in docs:
            dici = doc.to_dict()
            #if data["name"] == dici['name'] and data["other"] == dici['Project']and data["Project"] == dici['Project']:
            
            if data["name"] == dici['name'] and data["other"] == dici['other']:
                canAddProject = False

        if canAddProject:
            db.collection(u'ProjectTabel').document().set(data)
            flash("add new project  ")
        else:
            flash(" Project didnt added ")

        return redirect(url_for('addProject'))
    return render_template('addProject.html', form=form)


@app.route('/deleteProject', methods =['GET','POST'])
def deleteProject():
    form = DeleteProjectForm()
    if form.validate_on_submit():

        req = request.form
        email = req["email"]
        Project  = req["Project"]

        docs = db.collection(u'ProjectTabel').stream()
        for doc in docs:
            dici = doc.to_dict()
            if email == dici['name'] and Project  == dici['other']:
                print (f"ProjectTabel {dici['name']} in {dici['other']} has beem deleted")
                db.collection(u'ProjectTabel').document(doc.id).delete()
                flash("Delete Project")


        return redirect(url_for('deleteProject'))
    return render_template('DeleteProject.html', form=form)

@app.route('/addSprint', methods =['GET','POST'])
def addSprint():
    form = addSprintForm()
    if form.validate_on_submit():
        data = {
        "name": form.email.data,
        "other": form.Sprint.data,
        #"other": form.demandNumber.data,
        #" Demand": form. Demand.data,

        
        }
        docs = db.collection(u'SprintTabel').stream()
        canAddSprint = True
        for doc in docs:
            dici = doc.to_dict()
            #if data["name"] == dici['name'] and data["other"] == dici['Sprint']and data["Sprint"] == dici['Sprint']:
            
            if data["name"] == dici['name'] and data["other"] == dici['other']:
                canAddSprint = False

        if canAddSprint:
            db.collection(u'SprintTabel').document().set(data)
            flash("add new sprint  ")
        else:
            flash(" Sprint didnt added ")

        return redirect(url_for('addSprint'))
    return render_template('addSprint.html', form=form)


@app.route('/deleteSprint', methods =['GET','POST'])
def deleteSprint():
    form = DeleteSprintForm()
    if form.validate_on_submit():

        req = request.form
        email = req["email"]
        Sprint  = req["Sprint"]

        docs = db.collection(u'SprintTabel').stream()
        for doc in docs:
            dici = doc.to_dict()
            if email == dici['name'] and Sprint  == dici['other']:
                print (f"SprintTabel {dici['name']} in {dici['other']} has beem deleted")
                db.collection(u'SprintTabel').document(doc.id).delete()
                flash("Delete Sprint")


        return redirect(url_for('deleteSprint'))
    return render_template('DeleteSprint.html', form=form)

@app.route('/list', methods=['GET'])
def allDemands():
    
    guests=db.collection(u'DemandsTaple').stream()
    return render_template('AllDemnads.html', guests=guests)




if __name__ == '__main__':
    app.run(debug=True)
