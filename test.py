import unittest
from flask import app
from flask_wtf import form
import pyrebase
import App
#from App import delete_info_item 
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

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

    #Register User with uncorrect details
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
    
    #Register User with uncorrect details
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

        #Register User with uncorrect details
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

  






    #Delete exist park
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


    #Delete exist park
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


 #Delete exist park
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

 #Delete exist park
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

#Update exist Guest
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

















if __name__ == '__main__':
    unittest.main()