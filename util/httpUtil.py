import requests
import json
from common.commonData import CommonData
class HttpUtil:
    def __init__(self):
        self.http=requests.session()
        self.headers={'Content-Type':'application/json;charset=utf-8'}
    def post(self,path,data):
        proxies=CommonData.proxies
        host=CommonData.host
        data_json=json.dumps(data)
        if CommonData.token is not None:
            self.headers["token"]=CommonData.token
        resp_login=self.http.post(url=host+path,
                           proxies=proxies,
                           data=data_json,
                           headers=self.headers)
        resp_json=resp_login.text
        resp_dict=json.loads(resp_json)
        return resp_dict