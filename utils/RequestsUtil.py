import requests


class Request:
    def requests_api(self, url, data=None,json=None, headers=None, cookines=None,method='get'):
        if str( method ).lower() == "get":
            r=requests.get( url, data=data,headers=headers,cookines=cookines )
        elif str( method ).lower() == "post":
            r=requests.get( url, data=data, json=json, headers=headers,cookines=cookines  )
        elif str( method ).lower() == "heard":
            r=requests.head( url, data=data, json=json, headers=headers,cookines=cookines  )
        elif str( method ).lower() == "delete":
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
