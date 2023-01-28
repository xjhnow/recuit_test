import unittest
from common.handlerequest import SendRequest
from unittestreport import ddt,list_data
from common.readeexcel import ReadExcel
from common.handlepath import DATADIR
import os
# from common.handleconfig import conf
import config
import re
from common.handlelog import log
from common.handle_data import replace_data
from common.connectdb import DB
from common.handle_data import CaseDate

case_file = os.path.join(DATADIR, "apicases.xlsx")

@ddt
class TestLogin(unittest.TestCase):
    excel = ReadExcel(case_file,'login')
    cases = excel.read_data()
    resquest = SendRequest()


    @classmethod
    def setUpClass(cls) -> None:
        db = DB()
        sql = "SELECT f_pwd FROM recruit_students.t_login_account WHERE f_laccount = 'admin'"
        password = db.find_one(sql)
        CaseDate.pwd = password['f_pwd']

    @list_data(cases)
    def test_login(self,case):
        url = config.url + case['url']
        method = case['method']
        headers = config.headers
        data = eval(replace_data(case['data']))
        expected_key = eval(case['expected'])['msg']
        response = self.resquest.send(url=url,method=method,headers=headers,param=data)
        res = response.text
        # print(res)
        try:
            res_msg = re.search(expected_key, res).group()
            self.assertEqual(expected_key,res_msg)
        except (AttributeError,AssertionError) as e:
            log.error('用例：{}---未通过'.format(case['title']))
            log.exception(e)
            print(f'失败原因：返回结果未匹配到：{expected_key}')
            raise e
        else:
            log.info('用例：{}---通过'.format(case['title']))


