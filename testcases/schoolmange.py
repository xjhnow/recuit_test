import unittest
import os
from common.handlepath import DATADIR
from common.handlerequest import SendRequest
from common.handleconfig import conf
from library.ddt import data,ddt
from common.readeexcel import ReadExcel
from common.handlelog import log
from common.handlecookies import GetCookies



case_file = os.path.join(DATADIR, "apicases.xlsx")

@ddt
class TestSchoolMange(unittest.TestCase):
    excel = ReadExcel(case_file,'schoolmange')
    cases = excel.read_data()
    resquest = SendRequest()


    @classmethod
    def setUpClass(cls):
        url = conf.get('env','url') + '/login/in'
        data = eval(conf.get('test_data','data'))
        headers = eval(conf.get('env','headers'))
        gc = GetCookies(url=url,headers=headers,data=data)
        cls.cookie = "JSESSIONID=" + gc.getcookies()


    @data(*cases)
    def test_schoolmange(self,case):
        print(case['url'])
        url = conf.get('env','url') + case['url']
        method = case['method']
        headers = eval(conf.get('env','headers'))
        headers['Cookie'] = self.cookie
        data = eval(case["data"])
        expected = eval(case['expected'])
        response = self.resquest.send(url=url,data=data,headers=headers,method=method)
        res = response.json()
        try:
            self.assertEqual(expected['code'],res['code'],)
            self.assertIn(expected['message'],res['message'])
        except AssertionError as e:
            log.error('用例：{}---未通过'.format(case['title']))
            log.exception(e)
            raise e
        else:
            log.info('用例：{}---通过'.format(case['title']))


