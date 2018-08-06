
from flask_restful import Api
from flask import Blueprint

api = Blueprint("api", __name__) # 设置蓝图
resource = Api(api)

from .view import Test,BasicList,Volum

resource.add_resource(Test, "/1") # 设置路由
resource.add_resource(BasicList, "/basics") # 设置路由
resource.add_resource(Volum, "/volums/<int:novelid>")