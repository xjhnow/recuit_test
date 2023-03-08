# import unittest
# import os
# from common.handlepath import CASEDIR,REPORTDIR
# # from HTMLTestRunnerNew import HTMLTestRunner
# from BeautifulReport import BeautifulReport
# from library.HTMLTestRunnerNew import HTMLTestRunner
# import datetime
#
#
# date = datetime.datetime.now().strftime("%Y-%m-%d%H%M")
#
#
# # 第一步：创建套件
# suite = unittest.TestSuite()
# # 第二步：加载用例到套件
# loader = unittest.TestLoader()
# suite.addTest(loader.discover(CASEDIR))
# report_file = os.path.join(REPORTDIR,date+"report1.html")
# # 第三步：执行用例
# runner = HTMLTestRunner(stream=open(report_file, "wb"),
#                         description="长垣县教育局招生录取系统",
#                         title="招生录取系统测试报告",
#                         tester="xjhnow"
#                         )
# runner.run(suite)
# br = BeautifulReport(suite)
# #
# # br.report("前程贷项目用例",filename=date+"report1.html",report_dir=REPORTDIR)
#
# # send_email(report_file,"py26测试报告最终版")


import unittest
from common.handlepath import CASEDIR
from common.handlepath import REPORTDIR
import datetime
from BeautifulReport import BeautifulReport
from common.deletereport import delete_report

date = datetime.datetime.now().strftime("%Y-%m-%d%H%M")

#第一步创建测试套件
suite = unittest.TestSuite()

#第二步加载用例到测试套件
loader = unittest.TestLoader()
suite.addTest(loader.discover(CASEDIR))

#超过5条报告自动删除
delete_report()

br = BeautifulReport(suite)
br.report("招生录取系统测试报告",filename=date+"report.html",report_dir=REPORTDIR)
