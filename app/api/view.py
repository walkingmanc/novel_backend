from flask_restful import Resource
from app.models  import *
from marshmallow import  pprint
from app.util import  make_json_result

class Test(Resource):
	def get(self):
		r= Basic.query.get(1)
		basicschema=BasicSchema()
		result=basicschema.dump(r)
		pprint(result)
		return make_json_result(data=result.data)
		#return {"id":{'add':145}}

class BasicList(Resource):
	def get(self):
		r = Basic.query.all()
		basicschema = BasicSchema(many=True)
		result = basicschema.dump(r)
		#pprint(result)
		return make_json_result(data=result.data)


class VolumList(Resource):
	def get(self,novelId):
		volumList=Volum.query.filter_by(novelId=novelId).order_by(Volum.volId).all()
		#volumList =Volum.query.all()
		volumschema =VolumSchema(many=True)
		result = volumschema.dump(volumList)
		# pprint(result)
		return make_json_result(data=result.data)

class SectionList(Resource):
	def get(self,volumId):
		sectList=Section.query.with_entities(Section.secId, Section.volId, Section.secName).filter_by(volId=volumId).all()
		#volumList =Volum.query.all()
		sectionshema =SectionSchema(many=True)
		result = sectionshema.dump(sectList)
		# pprint(result)
		return make_json_result(data=result.data)

class SectionOne(Resource):
	def get(self,secId):
		section=Section.query.filter_by(secId=secId).first()
		#volumList =Volum.query.all()
		sectionshema =SectionSchema()
		result = sectionshema.dump(section)
		# pprint(result)
		return make_json_result(data=result.data)