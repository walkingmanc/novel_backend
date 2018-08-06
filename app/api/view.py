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


