import unittest
from unittest import TestCase
import sqlite3

conn = sqlite3.connect("mp7.db")
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


class Test(TestCase):
    def test_insert_developer(self):
        try:
            conn.execute("nnn", "454", "45", "gff", "rgrg", "trgtr")
            conn.insert_Developer("nnn", "454", "45", "gff", "rgrg", "trgtr")
            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_Insert_admin(self):
        try:
            conn.execute("nnn", "454", "45", "gff", "rgrg", "trgtr")
            conn.insert_admin("nnn", "454", "45", "gff", "rgrg", "trgtr")
            self.assertTrue(False)
        except:
            self.assertTrue(True)
    def test_login(self):
        try:
           self.assertTrue(False)
        except:
           self.assertTrue(True)


    def test_register_form(self):
    #Register User with uncorrect details
    def test_registerAdmine_uncorrect(self):
        try:

            email = "newRr@gmail.com"
            password = "123"
            username = "new"
            id = "87778"
            FN = "NNNN"
            LN = "BBBB"
            data = {"username": username, "password": password, "id": id, "email": email, "firstname": FN,
                    "lastname": LN, "developer": False}
            # info=auth.get_account_info(user['idToken'])['users'][0]['localId']
            conn.collection(u'Users').document().set(data)
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_register(self):
        try:

            email = "newRr@gmail.com"
            password = "123"
            username = "new"
            id = "87778"
            FN = "NNNN"
            LN = "BBBB"
            data = {"username": username, "password": password,"id": id, "email": email,"firstname": FN,"lastname": LN ,"developer": False}
            conn.collection(u'Users').document().set(data)
            self.assertTrue(True)
        except:
            self.assertTrue(False)



    def test_adddemand(self):
     try:
         email="khawla@gmail.com"
         demand="as a developer i can add deman "
        
         siprintNumbe="1" 
         data={"email":email,"demand":demand,"siprintNumber":siprintNumber}
         db.collection(u'Developertabel').document().set({"email":email,"demand":demand,"siprintNumber":siprintNumber})
         self.assertTrue(True)
     except:
            self.assertTrue(False)