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
config = {
  "apiKey": "AIzaSyBqv6hHsWrb8PkbEDWzsfDPRMAdwCspGz8",
  "authDomain": "codejanaflask.firebaseapp.com",
  "databaseURL":"https://codejanaflask-default-rtdb.firebaseio.com/",
  "projectId": "codejanaflask",
  "storageBucket": "codejanaflask.appspot.com",
  "messagingSenderId": "592871149231",
  "appId": "1:592871149231:web:a54baa8ee3a7e768764e5a",
  "measurementId" : "G-RELFYHWY68"
}




cred = credentials.Certificate('codejanaflask-firebase-adminsdk-kacfh-8b87d655e1.json')
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



#newManal
@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')



@app.route('/loginDeveloper',methods=['GET', 'POST'])
def loginDeveloper():
    form = LoginForm()
    if form.validate_on_submit():
        try:
            auth.sign_in_with_email_and_password(form.email.data,form.password.data)
            session["userdeveloper"]=form.email.data
            return redirect(url_for("userdeveloper"),form=form,developer=session["userdeveloper"])
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
            return redirect(url_for("scrumMaster"))
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

#ayam 
@app.route('/logout')
def logoutScrumMaster():
    session.pop("userScrumMaster",None)
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

@app.route('/deleteDeman/<string:email>/delete', methods =['GET','POST'])
def deleteDeman(email):
    
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

    form = DeleteDemanForm()
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
        return redirect(url_for('home', email=emailDemand))
    elif request.method == 'GET':
        print("get")
        docs
        form.email.data = wanted['email']
        form.Demand.data = wanted['demand']
        form.status.data=wanted['status']
      


        req = request.form
        email = req["email"]
        Demand  = req["Demand"]

        docs = db.collection(u'DemandsTaple').stream()
        for doc in docs:
            dici = doc.to_dict()
            if email == dici['email'] and Demand  == dici['demand']:
                print (f"DemandTabel {dici['email']} in {dici['demand']} has beem deleted")
                db.collection(u'DemandsTaple').document(doc.id).delete()
                flash("Delete Deman")


        return redirect(url_for('deleteDeman'))
    return render_template('DeleteDeman.html', form=form)












@app.route('/addDemandd', methods =['GET','POST'])
def addDemandd():
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

@app.route('/deleteDemandd', methods =['GET','POST'])
def deleteDemandd():
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

    
#newManal
@app.route('/myDemands/<string:email>/list', methods=['POST','GET'])
def myDemands(email):
    try:
        collection = db.collection("DemandsTaple").where(u"email", u"==", email).get()
    
        return render_template('myDemandlist.html',collection=collection)
    except Exception as e:
        return f"An Error Occured: {e}"


@app.route('/developerUsers', methods=['POST','GET'])
def developerUsers():
    guests=db.collection(u'Developertabel').stream()
    return render_template('developerUsers.html', guests=guests)

@app.route('/scrumMasterUsers', methods=['POST','GET'])
def scrumMasterUsers():
    guests=db.collection(u'ScrumMastertabel').stream()
    return render_template('scrumMasterUsers.html', guests=guests)

'''
@app.route('/listScrumMaster', methods=['GET'])
def allScrumMaster():
    
    guests=db.collection(u'ScrumMastertabel').stream()
    return render_template('AllScrumMaster.html', guests=guests)

    
@app.route('/myScrumMaster/<string:email>/list', methods=['POST','GET'])
def myScrumMaster(email):
    try:
        collection = db.collection("ScrumMaster").where(u"email", u"==", email).get()
    
        return render_template('myScrumMasterlist.html',collection=collection)
    except Exception as e:
        return f"An Error Occured: {e}"
'''
if __name__ == '__main__':
    app.run(debug=True)