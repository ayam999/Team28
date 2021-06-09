import unittest
from flask import app
from flask_wtf import form
import pyrebase
import App
#from App import delete_info_item 
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from App import app
import json 
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



db = firestore.client()
firebase = pyrebase.initialize_app(config)
auth= firebase.auth()

class TestHello(unittest.TestCase):
    #1
    def test_registerAdmine(self):
     try:
         email="bushra@gmail.com"
         firstname="bushra"
         id="123456789"
         lastname="alh"
         password="12345678" 
         data={"email":email,"firstname":firstname,"id":id,"lastname":lastname,"password":password}
         db.collection(u'Adminetabel').document().set(data)
         self.assertTrue(True)
     except:
            self.assertTrue(False)

    #2
    def test_registerAdmine_uncorrect(self):
        try:
    
            email="bushra"
            firstname="bu"
            id="12389"
            lastname="alh"
            password="12345678"
            data={"email":email,"firstname":firstname,"id":id,"lastname":lastname,"password":password}
            db.collection(u'Adminetabel').document().set(data)
            self.assertTrue(False)
        except:

            self.assertTrue(True)
    
    #3
    def test_registeScrumMaster_correct(self):
        try:
    
            email="dodo@gmail.com"
            firstname="bu"
            id="12355559"
            lastname="alh"
            password="12345678"
            data={"email":email,"firstname":firstname,"id":id,"lastname":lastname,"password":password}
            db.collection(u'ScrumMastertabel').document().set(data)
            self.assertTrue(False)
        except:
            self.assertTrue(True)

    #4
    def test_registeScrumMaster_uncorrect(self):
        try:
    
            email="dodo@gmail.com"
            firstname="bu"
            id="12355559"
            lastname="alh"
            password="12345678"
            data={"email":email,"firstname":firstname,"id":id,"lastname":lastname,"password":password}
            db.collection(u'ScrumMastertabel').document().set(data)
            self.assertTrue(False)
        except:

            self.assertTrue(False)

    #5
    def test_adddemand(self):
     try:
         demand="as a developer "
         email="naema@gmail.com"
         status="to do"
        
         siprintNumbe="1" 
         data={"email":email,"demand":demand,"status":status}
         db.collection(u'DemandsTaple').document().set({"demand":demand,"email":email,"status":status})
         self.assertTrue(True)
     except:
            self.assertTrue(False)

    #6
    def test_falladddemand(self):
     try:
         demand="as a developer i can add deman "
         email="khawla@gmail.com"
         status="To do"
        
         siprintNumbe="1" 
         data={"email":email,"demand":demand,"status":status}
         db.collection(u'DemandsTaple').document().set({"demand":demand,"email":email,"status":status})
         self.assertTrue(False)
     except:
            self.assertTrue(False)

    #7
    def test_correctadddemand(self):
     try:
         demand="as a developer i can add deman "
         email="khawla@gmail.com"
         status="To do"
        
         siprintNumbe="1" 
         data={"email":email,"demand":demand,"status":status}
         db.collection(u'DemandsTaple').document().set({"demand":demand,"email":email,"status":status})
         self.assertTrue(True)
     except:
            self.assertTrue(False) 

    #8   
    def test_registerdeveloper(self):
     try:
         email="mmm@gmail.co"
         firstname="gggg"
         id="000111110"
         lastname="ggg"
         password="123456"
         data={"email":email,"firstname":firstname,"id":id,"lastname":lastname,"password":password}
         db.collection(u'Adminetabel').document().set(data)
         self.assertTrue(True)
     except:
            self.assertTrue(False)
   

    #9
    def test_fallregisterdeveloper(self):
     try:
         email="55@gmail.co"
         firstname="ff"
         id="66666"
         lastname="fff"
         password="12333"
         data={"email":email,"firstname":firstname,"id":id,"lastname":lastname,"password":password}
         db.collection(u'Adminetabel').document().set(data)
         self.assertTrue(False)
     except:
            self.assertTrue(False)
   

    #10
    def test_delete_developer(self):
        try:
            email="newRr@gmail.com"
            firstname="ff"
            docs=db.collection(u'Users').stream()
            for doc in docs:
                d=doc.to_dict()
                if email==d['email'] and firstname==d['firstname']:
                    db.collection(u'Users').document(doc.id).delete()
                    return self.assertTrue(True)
        except:
            self.assertTrue(False)

    #11
    def test_delete_falldeveloper(self):
        try:
            email="newRr@gmail.com"
            firstname="ff"
            docs=db.collection(u'Users').stream()
            for doc in docs:
                d=doc.to_dict()
                if email==d['email'] and firstname==d['firstname']:
                    db.collection(u'Users').document(doc.id).delete()
                    return self.assertTrue(False)
        except:
            self.assertTrue(False)
    
    #12
    def test_delete_ScrumMaster(self):
        try:
            email="dodo@gmail.com"
            firstname="nbzm"
            docs=db.collection(u'Users').stream()
            for doc in docs:
                d=doc.to_dict()
                if email==d['email'] and firstname==d['firstname']:
                    db.collection(u'Users').document(doc.id).delete()
                    return self.assertTrue(True)
        except:
            self.assertTrue(False)

    #13
    def test_delete_FailedScrumMaster(self):
        try:
            email="hajks@gmail.com"
            firstname="jakeshan"
            docs=db.collection(u'Users').stream()
            for doc in docs:
                d=doc.to_dict()
                if email==d['email'] and firstname==d['firstname']:
                    db.collection(u'Users').document(doc.id).delete()
                    return self.assertFalse(False)
        except:
            self.assertTrue(True)

    #14
    def test_updateScrumMaster(self):
        try:
            ref_comment=db.collection(u'Users')
            email="teshela@gmail.com"
            ref_my=ref_comment.where(u'email',u'==',email).get()
            field_updates={"firstname":'דני',"id":'9816532',"lastname":'dedosam'}
            for r in ref_my:
                rr=ref_comment.document(r.id)
                rr.update(field_updates)
                self.assertTrue(True)
        except:
            self.assertTrue(False)

    #15
    def test_FailedUpdateScrumMaster(self):
        try:
            ref_comment=db.collection(u'Users')
            email="teshela@gmail.com"
            ref_my=ref_comment.where(u'email',u'==',email).get()
            field_updates={"firstname":'דני',"id":'9816532',"lastname":'dedosam'}
            for r in ref_my:
                rr=ref_comment.document(r.id)
                rr.update(field_updates)
                self.assertFalse(True)
        except:
            self.assertFalse(False)

  
    #16
    def test_delete_Project(self):
        try:
            parkName = "newTestPark"
            parkAddress = "bialik"

            docs = db.collection(u'Parks').stream()
            for doc in docs:
                dici = doc.to_dict()
                if parkName == dici['name'] and parkAddress == dici['other']:
                    #print (f"park {dici['name']} in {dici['other']} has beem deleted")
                    db.collection(u'Parks').document(doc.id).delete()
                    self.assertTrue(True)
        except:
            self.assertTrue(False)


    #17
    def test_delete_fallProject(self):
        try:
            parkName = "ghvgh"
            parkAddress = "biajhvhglik"

            docs = db.collection(u'Parks').stream()
            for doc in docs:
                dici = doc.to_dict()
                if parkName == dici['name'] and parkAddress == dici['other']:
                    #print (f"park {dici['name']} in {dici['other']} has beem deleted")
                    db.collection(u'Parks').document(doc.id).delete()
                    self.assertFalse(False)
        except:
            self.assertTrue(False)


    #18
    def test_delete_fallsprint(self):
        try:
            parkName = "ssss"
            parkAddress = "edee"

            docs = db.collection(u'Parks').stream()
            for doc in docs:
                dici = doc.to_dict()
                if parkName == dici['name'] and parkAddress == dici['other']:
                    #print (f"park {dici['name']} in {dici['other']} has beem deleted")
                    db.collection(u'Parks').document(doc.id).delete()
                    self.assertFalse(False)
        except:
            self.assertTrue(False)

    #19
    def test_delete_sprint(self):
        try:
            parkName = "dddd"
            parkAddress = "ffff"

            docs = db.collection(u'Parks').stream()
            for doc in docs:
                dici = doc.to_dict()
                if parkName == dici['name'] and parkAddress == dici['other']:
                    #print (f"park {dici['name']} in {dici['other']} has beem deleted")
                    db.collection(u'Parks').document(doc.id).delete()
                    self.assertFalse(False)
        except:
            self.assertTrue(False)

    #20
    def test_updatedeveloper(self):
        try:
            ref_comment=db.collection(u'Users')
            email="testttt@gmail.com"
            ref_my=ref_comment.where(u'email',u'==',email).get()
            field_updates={"firstname":'דני',"id":'12653',"lastname":'kecjkdsn'}
            for r in ref_my:
                rr=ref_comment.document(r.id)
                rr.update(field_updates)
                self.assertTrue(True)
        except:
            self.assertTrue(False)

    
    #21
    def test_fallupdatedeveloper(self):
        try:
            ref_comment=db.collection(u'Users')
            email="tejgjytt@gmail.com"
            ref_my=ref_comment.where(u'email',u'==',email).get()
            field_updates={"firstname":'דני',"id":'123',"lastname":'ghgfcgf'}
            for r in ref_my:
                rr=ref_comment.document(r.id)
                rr.update(field_updates)
                self.assertFalse(False)
        except:
            self.assertFalse(False)


#Update exist Guest
    def test_updatededemand(self):
        try:
            ref_comment=db.collection(u'Users')
            email="hjhhjhj@gmail.com"
            ref_my=ref_comment.where(u'email',u'==',email).get()
            field_updates={"firstname":'mmmmmmmmmm',"id":'1264453',"lastname":'mmmmmmmmmmm'}
            for r in ref_my:
                rr=ref_comment.document(r.id)
                rr.update(field_updates)
                self.assertTrue(True)
        except:
            self.assertTrue(False)






#Update exist Guest
    def test_falupdatededemand(self):
        try:
            ref_comment=db.collection(u'Users')
            email="hjhhjhj@gmail.com"
            ref_my=ref_comment.where(u'email',u'==',email).get()
            field_updates={"firstname":'jhjj',"id":'1264453',"lastname":'mmmmmjjjjjjjjjmmm'}
            for r in ref_my:
                rr=ref_comment.document(r.id)
                rr.update(field_updates)
                self.assertTrue(False)
        except:
            self.assertTrue(False)



    def test_unexist_nnewdeletedeveloper(self):
        try:
            ref_comment=db.collection(u'Users')
            ref_my=ref_comment.where(u'email',u'==',"UserNotFound@gmail.com").get()
            for r in ref_my:
                rr=ref_comment.document(r.id)
                rr.delete()
                self.assertTrue(False)
        except:
              
            self.assertTrue(True)



    def test_addsprint(self):
        try:
            parkName = "dddd"
            parkAddress = "ffff"


            docs = db.collection(u'Parks').stream()
            for doc in docs:
                dici = doc.to_dict()
                if parkName == dici['name'] and parkAddress == dici['other']:
                    #print (f"park {dici['name']} in {dici['other']} has beem deleted")
                    db.collection(u'Parks').document(doc.id).set(parkName)
                    self.assertFalse(True)
        except:
            self.assertTrue(False)

    def test_addfalnewssprint(self):
        try:
            parkName = "dddd"
            parkAddress = "ffff"

            docs = db.collection(u'Parks').stream()
            for doc in docs:
                dici = doc.to_dict()
                if parkName == dici['name'] and parkAddress == dici['other']:
                    #print (f"park {dici['name']} in {dici['other']} has beem deleted")
                    db.collection(u'Parks').document(doc.id).set(parkName)
                    self.assertFalse(False)
        except:
            self.assertTrue(False)

class TestHello(unittest.TestCase):
    #User login with correct details
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_homePage(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')

    

    def test_login_logout(self):
        taster = app.test_client(self)
        rv = taster.post('/login' , data=dict(email="mor0981@gmail.com",password="123456"),follow_redirects=True)
        self.assertTrue(rv.status, '200 OK')
        self.assertFalse('ברוכים'.encode() in rv.data)
        rv= taster.get('/logout',follow_redirects=True)
        self.assertFalse('התנתקת בהצלחה'.encode() in rv.data)

    def test_login_session(self):
        taster = app.test_client(self)
        rv = taster.post('/login' , data=dict(email="mor0981@gmail.com",password="123456"),follow_redirects=True)
        rv = taster.get('/login',follow_redirects=True)
        self.assertFalse('ברוכים'.encode() in rv.data)
        rv= taster.get('/logout',follow_redirects=True)

    def test_delete_user(self):
        taster = app.test_client(self)
        rv = taster.post('/register' , data=dict(email="test@gmail.com",password="123456",name="test",last="test"),follow_redirects=True)
        rv = taster.post('/login' , data=dict(email="test@gmail.com",password="123456"),follow_redirects=True)
        rv = taster.post('/unregister' , data=dict(email="test@gmail.com",password="123456"),follow_redirects=True)
        rv = taster.post('/login' , data=dict(email="test@gmail.com",password="123456"),follow_redirects=True)
        self.assertFalse('שם משתמש או סיסמא לא נכונים'.encode() in rv.data)

    def test_comment(self):
        taster = app.test_client(self)
        rv = taster.post('/register' , data=dict(email="test2@gmail.com",password="123456",name="test",last="test"),follow_redirects=True)
        rv = taster.post('/login' , data=dict(email="test2@gmail.com",password="123456"),follow_redirects=True)
        rv = taster.post('/comments/פארק%20ליכטנשטיין',data=dict(comment="test"),follow_redirects=True)
        rv = taster.get('/comments/פארק%20ליכטנשטיין')
        self.assertFalse('test'.encode() in rv.data)
        rv = taster.post('/unregister',data=dict(email="test2@gmail.com",password="123456"),follow_redirects=True)



    def test_login_as_admin(self):
        taster = app.test_client(self)
        rv = taster.post('/login' , data=dict(email="mor0981@gmail.com",password="123456"),follow_redirects=True)
        rv = taster.get('/login',follow_redirects=True)
        rv= taster.get('/logout',follow_redirects=True)
        self.assertFalse('test'.encode() in rv.data)
    def test_login_as_visit(self):
        taster = app.test_client(self)
        rv = taster.post('/login' , data=dict(email="dani@gmail.com",password="123456"),follow_redirects=True)
        rv = taster.get('/login',follow_redirects=True)
        self.assertFalse('משתמשים'.encode() in rv.data)
        rv= taster.get('/logout',follow_redirects=True)

    
    def test_add_admin(self):
        taster = app.test_client(self)
        rv = taster.post('/login' , data=dict(email="mor0981@gmail.com",password="123456"),follow_redirects=True)
        rv = taster.get('/login',follow_redirects=True)
        rv = taster.post('/registerByAdmin' , data=dict(name="טסט",last="טסט",email="test3@gmail.com",password="123456",Admin="true"),follow_redirects=True)
        rv= taster.get('/logout',follow_redirects=True)
        rv = taster.post('/login' , data=dict(email="test3@gmail.com",password="123456"),follow_redirects=True)
        self.assertFalse('ברוכים'.encode() in rv.data)
        rv = taster.post('/unregister',data=dict(email="test3@gmail.com",password="123456"),follow_redirects=True)

        

    # def delet_comment(self):
    #     taster = app.test_client(self)
    #     rv = taster.post('/register' , data=dict(email="test3@gmail.com",password="123456",name="test",last="test"),follow_redirects=True)
    #     rv = taster.post('/login' , data=dict(email="test3@gmail.com",password="123456"),follow_redirects=True)
    #     rv = taster.post('/comments/פארק%20ליכטנשטיין',data=dict(comment="test"),follow_redirects=True)
    #     rv = taster.get('/comments/פארק%20ליכטנשטיין')
    #     self.assertTrue('test'.encode() in rv.data)

    
        

         
        
    # def test_correct(self):
    #     try:
    #         auth.sign_in_with_email_and_password("mor0981@gmail.com","123456")
    #         self.assertTrue(True)
    #     except:
    #         self.assertTrue(False)
    # #User login with incorrect details
    
    # def test_incorrect(self):
    #     try:
    #         auth.sign_in_with_email_and_password("mor081@gmail.com","12661266")
    #         self.assertTrue(False)
    #     except:
    #         self.assertTrue(True)
    






 




if __name__ == '__main__':
    unittest.main()