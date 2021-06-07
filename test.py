import unittest
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
    def test_registerAdmine(self):
     try:
         email="dodo@gmail.com"
         firstname="dodosam"
         id="123456789"
         lastname="dedosam"
         password="123456" 
         data={"email":email,"firstname":firstname,"id":id,"lastname":lastname,"password":password}
         db.collection(u'ScrumMastertabel').document().set(data)
         self.assertTrue(True)
     except:
            self.assertTrue(False)

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
         demand="as a developer i can add deman "
         email="khawla@gmail.com"
         status="To do"
        
         siprintNumbe="1" 
         data={"email":email,"demand":demand,"status":status}
         db.collection(u'DemandsTaple').document().set({"demand":demand,"email":email,"status":status})
         self.assertTrue(True)
     except:
            self.assertTrue(False)


    def test_passadddemand(self):
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
   

    def test_passdregisterdeveloper(self):
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
   








    



if __name__ == '__main__':
    unittest.main()