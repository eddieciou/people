import json
from flask import make_response


class ReturnCode:
    codeMsg ={
        0: '', # (OK)
        1: '異常錯誤'
    }

    @staticmethod
    def getResp(code=0, msg=None, data= None):
        rData = ReturnCode.genReturnData(code, msg, data)
        r = make_response(rData)
        r.headers['Content-Type'] = 'application/json; charset=utf-8'
        return r

    @staticmethod
    def genReturnData(code=0, msg=None, data= None):
        rtnDict = {
            "code": code,
            "msg" : msg if msg else ReturnCode.codeMsg.get(code, "")
        }
        rtnDict.update({"datas": data})
        return json.dumps(rtnDict), 200