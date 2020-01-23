from . import db,login_manager
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash


class User(db.Model,UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(255),unique= True,nullable=False)#why
    username =db.Column(db.String(255),unique =True,nullable=False)
    password_hash = db.Column(db.String())
    bio=db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    booking=db.relationship('Book', backref='book',lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)
        
    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.add(self)
        db.session.commit()

    def __repr__ (self):
        return f'User{self.username}'
    

class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Integer,primary_key = True)
    name= db.Column(db.String(60),nullable=False)
    age=db.Column(db.Integer,nullable=False)
    user_id= db.Column(db.Integer,db.ForeignKey('users.id'))

    def save_book(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Book {self.name}'

class Session(db.Model):

    __tablename__ = 'sessions'
      
    id=db.Column(db.Integer,primary_key=True)
    



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)