import requests

class SendRequest():

    def __init__(self):
        self.session = requests.session()


    def send(self,method,url,headers=None,data=None,param=None):

        method = method.lower()
        response = None

        if method == "get":
            response = self.session.get(url=url,headers=headers,params=param)
        elif method == "post_data":
            response = self.session.post(url=url, headers=headers, data=data)
        elif method == "post_json":
            response = self.session.post(url=url, headers=headers, json=data)

        return response
