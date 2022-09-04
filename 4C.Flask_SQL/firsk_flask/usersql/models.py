from firsk_flask import db


class User(db.Model):

    id=db.Column(db.Integer , primarty_key=True)
    username=db.Column(db.String(50),index=True,unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(120))

    def __repr__(self):
        return{
            'username':self.username,
            'password':self.password,
            'email':self.email
        }