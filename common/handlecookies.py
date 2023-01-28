import requests
from requests import utils
from common.handleconfig import conf


url = conf.get('env','url') + "/login/in?"
headers = eval(conf.get('env','headers'))
data = eval(conf.get('test_data','data'))


class GetCookies():

    def __init__(self,url,headers,data):
        self.session = requests.session()
        self.session.post(url=url, headers=headers, data=data)


    def getcookies(self):

        cookie = utils.dict_from_cookiejar(self.session.cookies)

        return cookie['JSESSIONID']



Cookies = GetCookies(url=url,headers=headers,data=data)
cookie = "JSESSIONID=" + Cookies.getcookies()


# print(cookie,type(cookie))
# session = requests.session()
# session.post(url=url,headers=headers,data=data)
# cookie = utils.dict_from_cookiejar(session.cookies)
# print(cookie['JSESSIONID'])