import unittest
import pyrebase
import App
from App import delete_info_item 
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
    #User login with correct details
    def test_correct(self):
        try:
            auth.sign_in_with_email_and_password("bushra@gmail.com","12345678")
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    #User login with uncorrect details
    def test_uncorrect(self):
        try:
            auth.sign_in_with_email_and_password("bushra@gmail.com","12345678")
            self.assertTrue(False)
        except:
            self.assertTrue(True)
    #Register User with correct details
    def test_register(self):
        try:
    
            email="newRr@gmail.com"
            password="123"
            username="new"
            #user=auth.create_user_with_email_and_password("newRr@gmail.com","123321")
            data={"username":username,"email":email,"password":password,"admin":False}
            #info=auth.get_account_info(user['idToken'])['users'][0]['localId']
            db.collection(u'Users').document().set(data)
            self.assertTrue(True)
        except:
            self.assertTrue(False)

   

if __name__ == '__main__':
    unittest.main()
    
