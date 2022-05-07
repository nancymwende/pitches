from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime

class Post(db.Model):
   __tablename__ = 'Posts'
   id = db.Column(db.Integer,primary_key = True)
   title = db.Column(db.String(255))
   category = db.Column(db.String)
   content = db.Column(db.Text)
   date_posted = db.Column(db.DateTime,default = datetime.utcnow)
   
   
   
   
   
   
   
class User(db.Model):
   __tablename__ = 'users'
   id = db.Column(db.Integer,primary_key = True)
   username = db.Column(db.String(255))
   
   
   
   @property
   def password(self):
      raise AttributeError('You cannot read the passwprd attribute')
      
   @password.setter
   def password(self,password):
      self.pass_secure = generate_password_hash(password)
   
   def verify_password(self,password):
      return check_password_hash(self.pass_secure, password)
   
   
   
   
   
   
   
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
   
   
   
