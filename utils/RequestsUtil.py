import requests
from utils.LogUtil import my_log

class Request:
    def __init__(self):
        self.log=my_log("Requests")
    def requests_api(self, url, data=None,json=None, headers=None, cookines=None,method='get'):
        if str( method ).lower() == "get":
            self.log.debug("发送GET请求")
            r=requests.get( url, data=data,headers=headers )
        elif str( method ).lower() == "post":
            self.log.debug( "发送POST请求" )
            r=requests.get( url, data=data, json=json, headers=headers,cookines=cookines  )
        elif str( method ).lower() == "heard":
            self.log.debug( "发送HEARD请求" )
            r=requests.head( url, data=data, json=json, headers=headers,cookines=cookines  )
        elif str( method ).lower() == "delete":
            self.log.debug( "发送DELETE请求" )
            r=requests.delete( url, data=data, json=json, headers=headers,cookines=cookines  )
        else:
            pass
        code=r.status_code
        try:
            body=r.json()
        except Exception as e:
            body=r.text
        res=dict()
        res['code']=code
        res['body']=body
        return res

    def get(self, url, **kwargs):
        return self.requests_api( url, method='get', **kwargs )

    def post(self, url, **kwargs):
        return self.requests_api( url, method='post', **kwargs )
