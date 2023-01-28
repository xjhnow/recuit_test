import os

#项目路径
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#测试用例目录路径
DATADIR = os.path.join(BASEDIR,"data")

#用例模块目录路径
CASEDIR = os.path.join(BASEDIR,'testcases')

#日志文件目录路径
LOGDIR = os.path.join(BASEDIR,'log')

#配置文件目录路径
CONFDIR = os.path.join(BASEDIR,"conf")

#测试报告目录路径
REPORTDIR = os.path.join(BASEDIR,"report")