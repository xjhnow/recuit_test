import unittest
from common.handlerequest import SendRequest
from library.ddt import ddt,data
from common.readeexcel import ReadExcel
from common.handlepath import DATADIR
import os
from common.handleconfig import conf
from common.handlelog import log
from common.handlecookies import cookie
import jsonpath
from common.connectdb import DB
import random


case_file = os.path.join(DATADIR, "apicases.xlsx")



@ddt
class TestSchoolMange(unittest.TestCase):
    excel = ReadExcel(case_file,'schoolmange')
    cases = excel.read_data()
    resquest = SendRequest()
    db = DB()


    @data(*cases)
    def test_login(self,case):
        url = conf.get('env', 'url') + case['url']
        method = case['method']
        headers = eval(conf.get('env', 'headers'))
        headers['Cookie'] = cookie
        case['data'] = case['data'].replace('#schoolName#', self.schoolname())
        data = eval(case['data'])
        expected = eval(case['expected'])
        response = self.resquest.send(url=url, data=data, headers=headers, method=method)
        res = response.json()
        if case["interface"] == 'manascho_create':
            school_id = jsonpath.jsonpath(res,'$..id')[0]

        try:
            self.assertEqual(expected['code'], res['code'])
            self.assertIn(expected['message'], res['message'])
            if case['check_sql']:
              sql = "SELECT * FROM recruit_students.t_school_info where f_id ={}".format(school_id)
              count = self.db.find_count(sql)
              self.assertEqual(1, count)
        except AssertionError as e:
            log.error('用例：{}---未通过'.format(case['title']))
            log.exception(e)
            raise e
        else:
            log.info('用例：{}---通过'.format(case['title']))


    def schoolname(self):
        while True:
            name = "这是新增学校"
            name += str(random.randint(0, 999))
            sql = f"SELECT * FROM recruit_students.t_school_info WHERE f_school_name LIKE '{name}'"
            count = self.db.find_count(sql)
            if count:
                continue
            else:
                return name





