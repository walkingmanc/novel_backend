from flask import jsonify
from app.code import Code


def make_json_result(data=None, code=Code.SUCCESS):
    #return jsonify({"code": code, "data": data, "msg": Code.msg[code]})
    
    
    return jsonify(code=code, data=data, msg=Code.msg[code])