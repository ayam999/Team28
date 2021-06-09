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



db = firestore.client()
firebase = pyrebase.initialize_app(config)
auth= firebase.auth()




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

    
        

         





    if __name__ == '__main__':
      unittest.main()



