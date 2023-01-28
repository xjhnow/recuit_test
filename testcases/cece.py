import requests
import jsonpath
import json
import random



url = 'http://192.168.2.83:8090/recruit.students/school/manage/updateSchoolInfo'
data2 = {'id':'249','isSelfEnrollment':'0','enrollment':0}
headers = {
  "Host": "192.168.2.83:8090",
  "Content-Length": "46",
  "Accept": "application/json, text/javascript, */*; q=0.01",
  "X-Requested-With": "XMLHttpRequest",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
  "Origin": "http://192.168.2.83:8090",
  "Referer": "http://192.168.2.83:8090/recruit.students/school/manage/index",
  "Accept-Encoding": "gzip",
  "Accept-Language": "zh-CN,zh;q=0.9",
  "Cookie": "JSESSIONID=5CDD00124C1F89049095A19CEFBAE491",
  "Connection": "keep-alive"
}


res = requests.post(url=url,headers=headers,data=data2)
print(res.json())
# b = {'code': 1, 'message': '学校创建成功，登录帐号为702902，密码为123456。', 'costTime': 0,
#      'data': {'id': 293, 'schoolName': '', 'schoolCode': None, 'canRecruit': '2', 'phone': None, 'name': None, 'schoolType': None, 'listSchoolType': [{'id': None, 'typeName': None, 'status': None, 'sort': 0}], 'isSelfEnrollment': '1', 'enrollment': None, 'isSelfEnrollmentTime': '1', 'startTime': None, 'endTime': None, 'isStudentRecruitTime': '1', 'recruitStartTime': None, 'recruitEndTime': None, 'province': None, 'city': None, 'county': None, 'area': None, 'status': '1', 'remark': '测测新增学校', 'createUser': 10000, 'createUserAccount': None, 'createTime': 1665319763977, 'updateUser': 10000, 'updateUserAccount': None, 'updateTime': 1665319763977, 'laccount': 702902, 'statisticDatas': None},
#      'start': 0, 'page': 0, 'total': 0}
#
# a = jsonpath.jsonpath(b,'$..i2d')[0]
# a = {'param': [1,2,3]}
# print(a['param'])
# body = json.dumps(a['param'])
# print(body)
from common.connectdb import DB
db = DB()


# def schoolname():
#   while True:
#     name = "樊屯小学"
#     name += str(random.randint(0, 2))
#     sql = f"SELECT * FROM recruit_students.t_school_info WHERE f_school_name LIKE '{name}'"
#     count = db.find_count(sql)
#     if not count:
#       return name
#     break
#
# print(schoolname())
# name2 = "樊屯小学1"
