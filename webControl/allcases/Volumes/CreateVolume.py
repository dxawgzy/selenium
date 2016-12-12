#-*- coding: utf-8 -*
import sys
import unittest
import os
sys.path.append(os.path.join('..', '..'))  #用于导入上两级目录中的模块
from basecontrol import BaseControl as _b
from base import Config as _c
from base import Volumes
from selenium.webdriver.common.keys import Keys

class CreateVolume(unittest.TestCase, Volumes):
    name_des = [
        'jue-1',
        'jue-2',
        'jue-3',
        'jue-4',
        'jue-5',
        'jue-6',
        #('jue-7', '111111111111111111111111111111')
        #('jue-8', '111111111111111111111111111111')
        #('jue-9', '111111111111111111111111111111')
    ]
    def setUp(self):
        self.c = _c()
        self.control = _b(self.c.server.url)
        self.control.login(self.c.user.user, self.c.user.passwd)
        self.control.click_link_by_text('存储')
        self.control.click_link_by_text('云硬盘')

    def test_create_volume(self):
        for name in self.name_des:
            self.control.click_button_by_text('新建')
            self.control.fill_input_after_label(u'名称*', name)
            self.control.fill_input_after_label(
                u'描述', u'自动化创建', self.control.TEXTAREA)
            self.control.fill_input_after_label(u'容量（GB）*', '1')
            self.control.choice_select_after_label(u'云硬盘类型', 'sas')
            self.control.choice_select_after_label(u'新建方式', u'没有源，空白云硬盘')
            self.control.click_button_by_text('确定')
            #self.control.send_keys(Keys.ENTER)

    def tearDown(self):
        pass
