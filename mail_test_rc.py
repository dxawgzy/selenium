# -*- coding: utf-8 -*-
from selenium import selenium
import unittest, time, re

class mail_test_rc(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        #self.selenium = selenium("localhost", 4444, "*chrome", "http://mail.163.com/")
        self.selenium = selenium("localhost", 4444, "*firefox D:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe", "http://mail.163.com/")
        self.selenium.start()
    
    def test_mail_test_rc(self):
        sel = self.selenium
        sel.open("/")
        sel.click("id=idPlaceholder")
        sel.type("id=idInput", "邮箱")
        sel.click("id=pwdInput")
        sel.type("id=pwdInput", "密码")
        sel.click("id=loginBtn")
#        sel.click("css=#_mail_component_51_51 > span.oz0")
#        sel.type("css=input.nui-editableAddr-ipt", "邮箱")
#        sel.click("id=_mail_input_3_204")
#        sel.type("css=#_mail_input_3_204 > input.nui-ipt-input", u"测试")
#        sel.click("css=#_mail_button_2_183 > span.nui-btn-text")
#        sel.click("id=_mail_link_25_227")
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

