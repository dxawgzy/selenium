# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Horizon1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://10.89.151.10/auth/login/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_horizon1(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("gzy")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("123456")
        driver.find_element_by_id("loginBtn").click()
        driver.find_element_by_xpath("//dt").click()               #Project
        driver.find_element_by_xpath("//dt[2]").click()            #Admin
        driver.find_element_by_link_text("Host Aggregates").click() #Admin
        driver.find_element_by_xpath("(//a[contains(text(),'Instances')])[2]").click() #Admin
        driver.find_element_by_link_text("Instances").click()       #Admin
        driver.find_element_by_xpath("//dt[2]").click()             #Admin
        driver.find_element_by_xpath("//dd[2]/div/h4").click()      #Admin
        driver.find_element_by_xpath("(//a[contains(text(),'Instances')])[2]").click() #Admin
        driver.find_element_by_link_text("Host Aggregates").click()  #Admin
        driver.find_element_by_link_text("Flavors").click()          #Admin
        driver.find_element_by_xpath("//dt").click()                 #Project
        driver.find_element_by_link_text("Instances").click()        #Project
        driver.find_element_by_link_text("gzy-key").click()          #Project
        driver.find_element_by_xpath("(//a[contains(text(),'Overview')])[3]").click() #Project下虚拟机gzy-Key的Overview
        driver.find_element_by_link_text("Volumes").click()
        driver.find_element_by_link_text("Images").click()
        driver.find_element_by_link_text("Access & Security").click() #实际运行时前两步在Admin下,这一步需先手动点击Project
        driver.find_element_by_xpath("//div[2]/h4").click()           #Project下第二项Network
        driver.find_element_by_link_text("Network Topology").click()  #Network下
        driver.find_element_by_xpath("//div[3]/h4").click()           #Project下第三项Orchestration
        driver.find_element_by_link_text("Stacks").click()            #Orchestration下
        driver.find_element_by_xpath("//dt[2]").click()               #Admin
        driver.find_element_by_link_text("System Information").click()
        driver.find_element_by_xpath("//dt[3]").click()               #Identity
        driver.find_element_by_link_text("Projects").click()
        driver.find_element_by_link_text("Users").click()
        driver.find_element_by_xpath("//dt[2]").click()               #Admin
        driver.find_element_by_link_text("Metadata Definitions").click()
    
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
