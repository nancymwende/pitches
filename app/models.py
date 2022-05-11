from . import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
   return User.query.get(int(user_id))


class Post(db.Model):
   __tablename__ = 'posts'
   id = db.Column(db.Integer,primary_key = True)
   title = db.Column(db.String(255))
   category = db.Column(db.String)
   content = db.Column(db.Text)
   user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
   date_posted = db.Column(db.DateTime,default = datetime.utcnow)


class User(UserMixin,db.Model):
   __tablename__ = 'users'
   id = db.Column(db.Integer,primary_key = True)
   username = db.Column(db.String(255))
   email = db.Column(db.String(255), unique = True,index = True)
   bio = db.Column(db.String(255))
   profile_pic_path = db.Column(db.String())
   password_hash = db.Column(db.String(255))
   user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
   posts = db.relationship('Post',backref = 'posts',lazy = 'dynamic')
   
   @property
   def password(self):
      raise AttributeError('You cannot read the passwprd attribute')
      
   @password.setter
   def password(self,password):
      self.password_hash = generate_password_hash(password)
   
   def verify_password(self,password):
      return check_password_hash(self.password_hash, password)
   
class Upvote(db.Model):
   __tablename__ = 'upvotes'
   id = db.Column(db.Integer,primary_key = True)
   user_id = db.Column(db.Integer)
   
   

class Downvote(db.Model):
   __tablename__ = 'downvotes'
   id = db.Column(db.Integer,primary_key = True)
   user_id = db.Column(db.Integer)
   
class Comment(db.Model):
   __tablename__ = 'comments'
   id = db.Column(db.Integer, primary_key=True)
   comment = db.Column(db.String(255))
   user_id = db.Column(db.Integer)
   
   
   
