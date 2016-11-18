# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Horizon(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        # self.base_url = "https://10.89.151.10"
        self.base_url = "http://10.127.2.31"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_horizon(self):
        driver = self.driver
        driver.get(self.base_url + "/auth/login/")
        # driver.get(self.base_url)
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("admin")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("Abc12345")
        driver.find_element_by_id("loginBtn").click()
        driver.find_element_by_xpath("//dt[1]").click()
        driver.find_element_by_xpath("//div/h4").click()
        #driver.find_element_by_xpath("//div/ul/li[2]").click()
        driver.find_element_by_link_text("Instances").click()
        # driver.find_element_by_link_text("gzy-key").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Console')])[2]").click()   #Project下的虚拟机
        #driver.find_element_by_xpath("(//a[contains(text(),'Console')])[2]").click()  #Admin下的虚拟机
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

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
