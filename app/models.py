from app import db
from datetime import datetime


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
     	username = db.Column(db.String(20), index=True, unique=True)
     	password = db.Column(db.String(64), index=True)
     	email = db.Column(db.String(64), index=True, unique=True)


     	def is_authenticated(self):
        	 return True
     	def is_active(self):
        	 return True
     	def is_anonymous(self):
        	 return False
     	def get_auth_token(self):
        	 return unicode(hashlib.sha1(self.username +
        	self.password).hexdigest())
     	def get_id(self):
        	 return unicode(self.id)
     	def __repr__(self):
        	 return '<User %r>' % (self.username)

		

class Projects(db.Model):
	
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(20), index=True)
	description = db.Column(db.String(1000), index=True)
	button_list_title = db.Column(db.String(30), index=True)
	button_list_url = db.Column(db.String(30), index=True)
	tags = db.Column(db.String(20), index=True)
	file = db.Column(db.Unicode(1000))
	file2 = db.Column(db.Unicode(1000))
	
	
	def __init__ (self, title, description, button_list_title, button_list_url, tags, file, file2):
		self.title = title
		self.description = description
		self.button_list_title = button_list_title
		self.button_list_url = button_list_url
		self.tags = tags 
		self.file = file
		self.file2 = file2
		

	