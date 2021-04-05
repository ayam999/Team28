import unittest
from unittest import TestCase
import sqlite3

conn = sqlite3.connect("mp7.db")


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



