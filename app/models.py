from .exts import db
from flask import jsonify
from marshmallow import Schema, fields



class Basic(db.Model):
	__tablename__='basic'
	novelId = db.Column(db.Integer, primary_key=True,autoincrement=True)
	novelName = db.Column(db.String(100), nullable=False)
	picUrl = db.Column(db.String(50), nullable=False)
	descp = db.Column(db.String(100), nullable=False)
	author = db.Column(db.String(20))
	catg = db.Column(db.String(20))

	def __repr__(self):
		return '{"novelName"："%s"}' % (self.novelName)


  
class BasicSchema(Schema):
	novelId = fields.Integer()
	novelName = fields.Str()
	picUrl =fields.Str()
	descp = fields.Str()
	author = fields.Str()
	catg = fields.Str()

