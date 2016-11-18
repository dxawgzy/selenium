#-*- coding: utf-8 -*
import sys
import unittest
import os
import time
sys.path.append(os.path.join('..', '..'))  #用于导入上两级目录中的模块
from basecontrol import BaseControl as _b
from base import Config as _c
from base import Snapshots

class CreateSnapshot(unittest.TestCase, Snapshots):
    def setUp(self):
        self.c = _c()
        self.control = _b(self.c.server.url)
        self.control.login(self.c.user.user, self.c.user.passwd)
        self.control.click_link_by_text('存储')
        self.control.click_link_by_text('云硬盘')

    def test_create_snapshot(self):
        time.sleep(5)
        for i in range(0,10):
            self.control.click_by_text('''
                                            相关操作
                                            ''', 2)
            self.control.click_by_text('创建快照')
            self.control.fill_input_after_label('快照名*', 'autocreate-%d' %i)
            self.control.fill_input_after_label('描述', 'autocreate')
            self.control.click_button_by_text('创建')
            time.sleep(1)

    def tearDown(self):
        pass
