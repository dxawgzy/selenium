#coding=utf-8

import HTMLTestRunner
import unittest
import time
from base import Config as _c
from basecontrol import BaseControl as _b
from base import Volumes as vol
from base import Snapshots as ss
from allcases import Volumes
from allcases import Snapshots

BASE_CLS = {'Volumes': 'vol',
            'Snapshots': 'ss',}

if __name__ == '__main__':
    config = _c()
    suite = unittest.TestSuite()
    test_cases = config.server.cases.split(',')  #针对allcases下的文件夹

    for cases in test_cases:   #遍历每一个文件夹，每个cases表示allcases下的一个文件夹
        # you will find all child class in the /allcases, it must the same as
        # the father class in the base.py
        case_cls = (    #得到每个py文件中的所有类，一个类即为一个case
            [cls.__name__ for cls in vars()[BASE_CLS[cases]].__subclasses__()])
        for one_case in case_cls:     #遍历一个py文件中的所有类
            case_model = '.'.join([cases, one_case, one_case])
            test_name =\
                [tn for tn in dir(eval(case_model)) if 'test_' in tn]
            suite.addTest(eval(case_model+'("' + test_name[0] +'")'))

    # runner = unittest.TextTestRunner()
    # runner.run(suite)

    #取当前时间
    now_time = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    #定义个报告存放路径，支持相对路径。
    filename = 'E:\\python\\selenium\\'+now_time+'_report.html'
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'OpenStack Horizon测试报告',
        description=u'用例执行结果：')
    #执行测试用例
    runner.run(suite)


