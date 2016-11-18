# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class MailTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url = "http://mail.163.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_mail(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("idPlaceholder").click()
        driver.find_element_by_id("idInput").clear()
        driver.find_element_by_id("idInput").send_keys("邮箱")
        driver.find_element_by_id("pwdInput").click()
        driver.find_element_by_id("pwdInput").clear()
        driver.find_element_by_id("pwdInput").send_keys("密码")
        driver.find_element_by_id("loginBtn").click()
    """
        driver.find_element_by_css_selector("#_mail_component_51_51 > span.oz0").click()
        driver.find_element_by_css_selector("input.nui-editableAddr-ipt").clear()
        driver.find_element_by_css_selector("input.nui-editableAddr-ipt").send_keys("邮箱")
        driver.find_element_by_id("_mail_input_3_204").click()
        driver.find_element_by_css_selector("#_mail_input_3_204 > input.nui-ipt-input").clear()
        driver.find_element_by_css_selector("#_mail_input_3_204 > input.nui-ipt-input").send_keys(u"测试")
        driver.find_element_by_css_selector("#_mail_button_2_183 > span.nui-btn-text").click()
        driver.find_element_by_id("_mail_link_25_227").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    """
    """
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
    """
if __name__ == "__main__":
    unittest.main()
