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
   upvotes = db.relationship('Upvote',backref = 'posts',lazy = 'dynamic')
   downvotes = db.relationship('Downvote',backref = 'posts',lazy = 'dynamic')
   
   
   def save_post(self):
      db.session.add(self)
      db.session.commit()


class User(UserMixin,db.Model):
   __tablename__ = 'users'
   id = db.Column(db.Integer,primary_key = True)
   username = db.Column(db.String(255))
   email = db.Column(db.String(255), unique = True,index = True)
   bio = db.Column(db.String(255))
   profile_pic_path = db.Column(db.String())
   password_hash = db.Column(db.String(255))
   user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
   posts = db.relationship('Post',backref = 'post',lazy = 'dynamic')
   upvotes = db.relationship('Upvote',backref = 'post',lazy = 'dynamic')
   downvotes = db.relationship('Downvote',backref = 'post',lazy = 'dynamic')
   
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
   user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
   post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
   
   
   def save(self):
      db.session.add(self)
      db.session.commit()
   @classmethod
   def get_upvotes(cls,id):
      upvotes = Upvote.query.filter_by(post_id=id).all()
      return upvotes
      
      
   def _repr_(self):
      return f'{self.user_id}:{self.post_id}'
   
   

class Downvote(db.Model):
   __tablename__ = 'downvotes'
   id = db.Column(db.Integer,primary_key = True)
   user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
   post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
   
   def save(self):
      db.session.add(self)
      db.session.commit()
   @classmethod
   def get_downvotes(cls,id):
      downvotes = Downvote.query.filter_by(post_id=id).all()
      return downvotes
      
      
   def _repr_(self):
      return f'{self.user_id}:{self.post_id}'
   
class Comment(db.Model):
   __tablename__ = 'comments'
   id = db.Column(db.Integer, primary_key=True)
   comment = db.Column(db.String(255))
   user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
   post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
   
   
   
