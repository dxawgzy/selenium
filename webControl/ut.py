#-*- coding: utf-8 -*-
import sys
import unittest
import os
import time
from base import Config as _c
from basecontrol import BaseControl as _b

class TestBase(object):
    def get_name(self, cls):
        return cls.__class__.__name__

class Login(unittest.TestCase, TestBase):
    def setUp(self):
        self.c = _c()
        self.base = _b(self.c.server.url)
        self.login = False

    def test_login(self):
        self.login = self.base.login(self.c.user.user, self.c.user.passwd)

    def tearDown(self):
        self.base.close_web()
        self.assertEqual(True, self.login)

class snapshot(unittest.TestCase, TestBase):
    def setUp(self):
        self.c = _c()
        self.base = _b(self.c.server.url)
        self.snapshot_dir = ''

    def test_login(self):
        #self.login = self.base.login(self.c.user.user, self.c.user.passwd)
        self.snapshot_dir = self.base.snapshot(self.get_name(self))

    def tearDown(self):
        self.base.close_web()
        self.assertEqual(True, os.path.exists(self.snapshot_dir))

class ClickButton(unittest.TestCase, TestBase):
    def setUp(self):
        self.c = _c()
        self.base = _b(self.c.server.url)
        self.base.login(self.c.user.user, self.c.user.passwd)

    def test_click(self):
        self.base.click_link_by_text('用户管理')
        self.base.click_link_by_text('用户管理', 1)
        #self.base.click_button('新建')

    def test_common_click(self):
        self.base.click_by_text('用户管理')
        self.base.click_by_text('用户管理', 1)
        self.base.click_by_text('新建')


    def tearDown(self):
        #self.assertEqual(True, os.path.exists(self.snapshot_dir))
        pass

class Input(unittest.TestCase, TestBase):
    def setUp(self):
        self.c = _c()
        self.base = _b(self.c.server.url)
        self.base.login(self.c.user.user, self.c.user.passwd)
        self.base.click_link_by_text('存储')
        self.base.click_link_by_text('云硬盘')
        self.base.click_button_by_text('新建')

    def test_fill_input_in_label(self):
        self.base.fill_input_after_label('名称*', '123')

    def test_choice_select_after_labe(self):
        self.base.choice_select_after_label('新建方式', '没有源，空白云硬盘')

    def test_input_choice(self):
        self.base.fill_input_after_label('名称*', '123')
        self.base.fill_input_after_label(
            '描述', u'自动化创建', self.base.TEXTAREA)
        self.base.fill_input_after_label('容量（GB）*', '1')
        self.base.choice_select_after_label('云硬盘类型', 'sas')
        self.base.choice_select_after_label('新建方式', '没有源，空白云硬盘')
        self.base.click_button_by_text('确定')
        assert self.base.verify_text('123'), 'not found!'

    def test_common_choice(self):
        self.base.fill_by_label_text('名称*', '123', self.base.FOLLOW)
        self.base.fill_by_label_text('新建方式', '没有源，空白云硬盘',\
            self.base.FOLLOW)

    def tearDown(self):
        #self.assertEqual(True, os.path.exists(self.snapshot_dir))
        pass

def main():
    c = _c()
    base = _b(c.server.url)
    #base.snapshot('test')
    #base.login(c.user.user, c.user.passwd)
    #base.click_button(c.leftbtn.cloud_database)
    #print _c().server.url
    #base.searchsth('haha')


if __name__ == '__main__':
    #unittest.main()
    #main()
    cases = ([cls.__name__ for cls in vars()['TestBase'].__subclasses__()])
    suite = unittest.TestSuite()
    #suite.addTest(Login("test_login"))
    #suite.addTest(ClickButton("test_click"))
    #suite.addTest(ClickButton("test_common_click"))
    #suite.addTest(Input("test_fill_input_in_label"))
    suite.addTest(Input("test_input_choice"))
    #suite.addTest(Input("test_common_choice"))
    #for case in cases:
        #test_name = [tn for tn in dir(eval(case)) if 'test_' in tn]
        #suite.addTest(eval(case+'("' + test_name[0] +'")'))

    runner = unittest.TextTestRunner()
    runner.run(suite)



