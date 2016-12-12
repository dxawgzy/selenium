#coding=utf-8

from selenium.webdriver.common.by import By

class LoginPageLocators(object):

    #Portal页面
    # username = (By.ID, 'exampleInputAmount')
    # passwd = (By.XPATH, '//input[@type="password"]')

    #Horizon页面
    username = (By.ID, 'id_username')
    passwd = (By.ID, 'id_password')

class CommonLocatorsTextXpath(object):
    button_xpath = '//button[text() = "%s"]'  # text()函数，文本定位
    label_xpath = '//label[text() = "%s"]'    # 没有用到label定位，且label基本无text
    option_xpath = '//option[text() = "%s"]'


class DatabaseCreate(object):
    pass


