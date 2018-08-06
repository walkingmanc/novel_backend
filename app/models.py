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


class Section(db.Model):
	__tablename__ ='section'
	secId = db.Column(db.Integer(20), primary_key=True, autoincrement=True)
	volId = db.Column(db.Integer(20), nullable=False)
	secName=db.Column(db.String(50), nullable=False)
	secContent = db.Column(db.Text, nullable=False)
def __repr__(self):
		return '{"secName"："%s"}' % (self.secName)


class SectionSchema(Schema):
	secId = fields.Integer()
	volId = fields.Integer()
	secName = fields.Str()
	secContent = fields.Str()

class Volum(db.Model):
	__tablename__ = 'volum'
	volId = db.Column(db.Integer(20), primary_key=True, autoincrement=True)
	novelId = db.Column(db.Integer(20), nullable=False)
	volName = db.Column(db.String(50), nullable=False)


	def __repr__(self):
		return '{"secName"："%s"}' % (self.secName)

class VolumSchema(Schema):
	volId = fields.Integer()
	novelId = fields.Integer()
	volName = fields.Str()





