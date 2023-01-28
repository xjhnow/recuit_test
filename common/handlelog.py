import logging
import os
from common.handlepath import LOGDIR

class HandleLog(object):

    @staticmethod
    def creat_logger():
        #创建收集器，设置收集等级
        mylog = logging.getLogger("xjhnow")
        mylog.setLevel("DEBUG")
        #创建输出到控制台的渠道，设置等级
        sh = logging.StreamHandler()
        sh.setLevel("DEBUG")
        mylog.addHandler(sh)
        #创建输出到文件的渠道，设置等级
        fh = logging.FileHandler(filename=os.path.join(LOGDIR,"log.log"),encoding="utf-8")
        fh.setLevel("ERROR")
        mylog.addHandler(fh)
        #设置日志输出格式
        formater = "%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s"
        fm = logging.Formatter(formater)
        sh.setFormatter(fm)
        fh.setFormatter(fm)


        return mylog

log = HandleLog.creat_logger()
