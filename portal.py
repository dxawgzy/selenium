# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Portal(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://10.89.154.2/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_portal(self):
        driver = self.driver
        driver.get(self.base_url + "/login/?next=/instance-manage/")
        driver.find_element_by_xpath("//input[@type='text']").clear()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("admin")
        driver.find_element_by_xpath("//input[@type='password']").clear()
        driver.find_element_by_xpath("//input[@type='password']").send_keys("1qaz@WSX")
        driver.find_element_by_xpath("(//input[@type='text'])[2]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys("lyhc")
        driver.find_element_by_xpath(u"//input[@value='登录']").click()
        driver.find_element_by_xpath("(//input[@type='text'])[2]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys("ynnp")
        driver.find_element_by_xpath(u"//input[@value='登录']").click()
        driver.find_element_by_css_selector("div.left-menu").click()
        driver.find_element_by_css_selector("div.fa.fa-cubes").click()
        driver.find_element_by_link_text(u"主机集群").click()
        driver.find_element_by_link_text(u"主机管理").click()
        driver.find_element_by_link_text(u"主机管理").click()
        driver.find_element_by_link_text(u"云主机管理").click()
        driver.find_element_by_link_text(u"云主机组").click()
        driver.find_element_by_link_text(u"云主机管理").click()
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
        driver.find_element_by_link_text("https://192.168.202.10:6080/vnc_auto.html?token=f5c7fa3f-3a33-4f9a-a809-3edecead4154").click()
        driver.find_element_by_css_selector("button.close").click()
        driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[11]").click()
        driver.find_element_by_link_text(u"服务器组").click()
        driver.find_element_by_css_selector("button.btn.btn-primary").click()
        driver.find_element_by_css_selector("button.close").click()
        driver.find_element_by_link_text(u"镜像管理").click()
        driver.find_element_by_link_text(u"隐藏镜像管理").click()
        driver.find_element_by_css_selector("div.fa.fa-globe").click()
        driver.find_element_by_link_text(u"网络拓扑").click()
        driver.find_element_by_link_text(u"私有网络").click()
        driver.find_element_by_link_text(u"虚拟网卡").click()
        driver.find_element_by_link_text(u"路由器").click()
        driver.find_element_by_link_text(u"公网").click()
        driver.find_element_by_css_selector("button.btn.btn-primary").click()
        driver.find_element_by_css_selector("button.btn.btn-primary").click()
        driver.find_element_by_css_selector("button.close").click()
        driver.find_element_by_link_text(u"安全").click()
        driver.find_element_by_link_text(u"安全").click()
        driver.find_element_by_link_text(u"安全").click()
        driver.find_element_by_link_text(u"防火墙").click()
        driver.find_element_by_link_text(u"安全组").click()
        driver.find_element_by_xpath("//div[@id='mCSB_1_container']/div/ul/li[5]/a/div[2]").click()
        driver.find_element_by_link_text(u"云硬盘").click()
        driver.find_element_by_link_text(u"云硬盘类型").click()
        driver.find_element_by_link_text(u"快照管理").click()
        driver.find_element_by_css_selector("div.fa.fa-users").click()
        driver.find_element_by_css_selector("div.fa.fa-file-text").click()
        driver.find_element_by_css_selector("div.fa.fa-list-alt").click()
        driver.find_element_by_css_selector("button.btn.btn-default").click()
        driver.find_element_by_css_selector("button.btn.btn-default").click()
        driver.find_element_by_css_selector("div.fa.fa-cubes").click()
        driver.find_element_by_link_text(u"主机管理").click()
        driver.find_element_by_css_selector("button.btn.btn-default").click()
        driver.find_element_by_link_text(u"服务器组").click()
        driver.find_element_by_css_selector("button.btn.btn-primary").click()
        Select(driver.find_element_by_name("policy")).select_by_visible_text("affinity")
        driver.find_element_by_xpath("(//input[@type='text'])[2]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys("123")
        driver.find_element_by_css_selector("div.modal-footer > button.btn.btn-primary").click()
        driver.find_element_by_xpath("//div[@id='myFrame']/div/div/div/div[2]/div/div[2]/div/fosp-checkbox-group/table/tbody/tr[9]/td/fosp-checkbox/label/label").click()
        driver.find_element_by_xpath("(//input[@type='checkbox'])[10]").click()
        driver.find_element_by_xpath("//div[@id='myFrame']/div/div/div/div[2]/div/div[2]/div/fosp-checkbox-group/table/tbody/tr[9]/td/fosp-checkbox/label/label").click()
        driver.find_element_by_xpath("(//input[@type='checkbox'])[10]").click()
        driver.find_element_by_xpath("//div[@id='myFrame']/div/div/div/div[2]/div/div[2]/div/fosp-checkbox-group/table/tbody/tr[9]/td/fosp-checkbox/label/label").click()
        driver.find_element_by_xpath("(//input[@type='checkbox'])[10]").click()
        driver.find_element_by_css_selector("button.btn.btn-default").click()
        driver.find_element_by_xpath("//div[@id='myFrame']/div/div/div/div[2]/div/div[2]/div/fosp-checkbox-group/table/tbody/tr[9]/td/fosp-checkbox/label/label").click()
        driver.find_element_by_xpath("(//input[@type='checkbox'])[10]").click()
        driver.find_element_by_css_selector("button.btn.btn-default").click()
        driver.find_element_by_css_selector("label.fit-checkbox-label").click()
        driver.find_element_by_css_selector("input.magic-checkbox.fit-checkbox-input").click()
        driver.find_element_by_css_selector("label.fit-checkbox-label").click()
        driver.find_element_by_css_selector("input.magic-checkbox.fit-checkbox-input").click()
        driver.find_element_by_css_selector("label.fit-checkbox-label").click()
        driver.find_element_by_css_selector("input.magic-checkbox.fit-checkbox-input").click()
        driver.find_element_by_css_selector("button.btn.btn-default").click()
        driver.find_element_by_xpath("//div[@id='myFrame']/div/div/div/div[2]/div/div[2]/div/fosp-checkbox-group/table/tbody/tr[9]/td/fosp-checkbox/label/label").click()
        driver.find_element_by_xpath("(//input[@type='checkbox'])[10]").click()
        driver.find_element_by_css_selector("button.btn.btn-danger").click()
        driver.find_element_by_css_selector("div.modal-footer > button.btn.btn-primary").click()
        driver.find_element_by_css_selector("button.btn.btn-default").click()
        driver.find_element_by_css_selector("button.btn.btn-default").click()
        driver.find_element_by_css_selector("button.btn.btn-default").click()
        driver.find_element_by_css_selector("button.btn.btn-default").click()
        driver.find_element_by_css_selector("button.close").click()
        driver.find_element_by_link_text(u"云主机组").click()
        driver.find_element_by_link_text(u"查看").click()
        driver.find_element_by_css_selector("div.modal-footer > button.btn.btn-primary").click()
        driver.find_element_by_link_text(u"云主机管理").click()
        driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[11]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[21]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[17]").click()
        driver.find_element_by_link_text("2").click()
        driver.find_element_by_link_text("3").click()
        driver.find_element_by_link_text("3").click()
        driver.find_element_by_xpath("//div[@id='myFrame']/div/div/div/div[2]/div/div[2]/div/fosp-checkbox-group/div/div/div/ul/li[5]/a/span").click()
        driver.find_element_by_xpath("(//button[@type='button'])[23]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[44]").click()
        driver.find_element_by_css_selector("div.left-menu").click()
        driver.find_element_by_link_text(u"进入订单").click()
        driver.find_element_by_link_text(u"概况").click()
        driver.find_element_by_link_text(u"查看详情").click()
        driver.find_element_by_id("from_date_elem_begin_time").click()
        driver.find_element_by_xpath("//table[@id='laydate_table']/tbody/tr/td[4]").click()
        driver.find_element_by_id("to_date_elem_begin_time").click()
        driver.find_element_by_xpath("//table[@id='laydate_table']/tbody/tr/td[6]").click()
        driver.find_element_by_css_selector("div.form-group.pull-right > button.btn.btn-default").click()
        driver.find_element_by_css_selector("div.btn-group > div").click()
        driver.find_element_by_link_text(u"退出").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
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
