#coding=utf-8
__author__ = 'igis_gzy'

from selenium.webdriver import FirefoxProfile
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time

class Baidu(unittest.TestCase):

    def setUp(self):

        # ProfilesIni allProfiles = new ProfilesIni()
        # FirefoxProfile profile = allProfiles.getProfile("default")
        # self.driver = new FirefoxDriver(profile)

        # profile = webdriver.FirefoxProfile()
        # profile.native_events_enabled = True
        # self.driver = webdriver.Firefox(profile)

        self.driver = webdriver.Firefox()
        # self.driver = webdriver.Ie()
        # options = webdriver.ChromeOptions()
        # options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
        # self.driver  = webdriver.Chrome(chrome_options=options)
        # self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = "http://www.baidu.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    #百度搜索用例
    def test_baidu_search(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").send_keys("selenium webdriver")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        driver.close()

    #百度设置用例
    # def test_baidu_set(self):
    #     driver = self.driver
    #     #进入搜索设置页
    #     driver.get(self.base_url + "/gaoji/preferences.html")
    #     #设置每页搜索结果为100 条
    #     m=driver.find_element_by_name("NR")
    #     m.find_element_by_xpath("//option[@value='100']").click()
    #     time.sleep(2)
    #     #保存设置的信息
    #     driver.find_element_by_xpath("/html/body/form/div/input").click()
    #     time.sleep(2)
    #     driver.switch_to_alert().accept()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()


