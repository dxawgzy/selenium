#coding=utf-8
__author__ = 'igis_gzy'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class Youdao(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        # self.driver = webdriver.Ie()
        self.driver.implicitly_wait(10)
        self.base_url = "http://www.youdao.com"
        self.verificationErrors = []
        self.accept_next_alert = True

    #有道搜索用例
    def test_youdao_search(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("query").send_keys(u"虫师")
        driver.find_element_by_id("qb").click()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()


