from codejana_flask import db
class developer(db.Model):
    username=db.Column(db.String(20),unique=true,nullable=False)
    password=db.Column(db.String(20),nullable=False)
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(120),unique=True,nullable=False)
    firstname=db.Column(db.String(20),unique=True,nullable=False)
    lastname=db.Column(db.String(20),unique=True,nullable=False)

    def __repr__(self):
        return f'{self.username}' : {self.password} : {self.id} :  {self.email} :{self.firstname} : {self.lastname} 

