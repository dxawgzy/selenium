#-*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from locators import LoginPageLocators as LPL
from locators import CommonLocatorsTextXpath as CL
import time
import os
from base import Config

# def use_dialog_first(fun):
#     def wrapper(*args, **kargs):
#
#         nowhandle = driver.current_window_handle
#         for handle in driver.window_handles:
#             if handle != nowhandle:
#                 driver.switch_to_window(handle)
#         func()
#     return wrapper()

class BaseControl(object):

    TEXTAREA = 'textarea'
    INPUT = 'input'
    OPTION = 'option'

    PAGEELEMENTS = {
        'TEXTAREA': TEXTAREA,
        'INPUT': INPUT,
        'OPTION': OPTION,
    }

    FOLLOW = '/following::%s'  #查找满足条件的下一个
    PRECED = '/preceding::%s'
    PARENT = '/parent::%s'

    def __init__(self, url):
        self.config = Config()
        # self.driver = webdriver.Chrome()
        # self.driver = webdriver.Ie()
        self.driver = webdriver.Firefox()
        self.driver.get(url)
        self.nowhandle = self.driver.current_window_handle
        # self.locator = ()


    def login(self, username, passwd):
        # log in with username and passwd
        self.driver.find_element(*LPL.username).send_keys(username)
        time.sleep(0.5)
        self.driver.find_element(*LPL.passwd).send_keys(passwd)
        time.sleep(0.5)
        self.driver.find_element(*LPL.passwd).send_keys(Keys.ENTER)
        for wait in range(0, int(self.config.server.waittimes)):
            time.sleep(0.5)
            if self.config.fitos.title not in self.driver.title:
                return False

        self.nowhandle = self.driver.current_window_handle
        return True

    def close_web(self):
        # close the browser, it is teardown
        time.sleep(1)
        self.driver.quit()

    def snapshot(self, name):
        # take snapeshot and save it in pictures/name
        time.sleep(0.5)
        base_dir = os.path.join(os.getcwd(), self.config.server.picdir)
        snapshot_dir = os.path.join(base_dir, name+'.png')
        self.driver.get_screenshot_as_file(snapshot_dir)
        return snapshot_dir

    # def click_button_by_text(self, type_button, index = 0):
    #     #WebDriverWait(self.driver, 10).until(
    #     #    lambda driver: driver.find_element(button))
    #     button_element = WebDriverWait(
    #         self.driver, int(self.config.server.waittimes)).until(lambda driver:
    #         driver.find_elements_by_xpath(CL.button_xpath %type_button))
    #     button_element[index].click()

    def click_button_by_text(self, type_button, index = 0):
        button_element = WebDriverWait(
            self.driver, int(self.config.server.waittimes)).until(lambda driver:
            driver.find_elements_by_xpath(CL.button_xpath %type_button))
        button_element[index].click()

    def click_link_by_text(self, type_link, index = 0):
        button_element = WebDriverWait(
            self.driver, int(self.config.server.waittimes)).until(lambda driver:
            driver.find_elements_by_link_text(type_link))

        button_element[index].click()

    def fill_input_after_label(self, label_text, text, input_type = 'input'):
        # <label> write something<\label>
        # <input type=blah>

        label_locator = CL.label_xpath %label_text

        input_element = WebDriverWait(
            self.driver, int(self.config.server.waittimes)).until(lambda driver:
            driver.find_element_by_xpath(
                                label_locator + '/following::' + input_type))

        input_element.send_keys(text)

    def choice_select_after_label(self, label_text, option):
        # <label> write something<\label>
        # <select >
        label_locator = CL.label_xpath %label_text

        select_element = WebDriverWait(
            self.driver, int(self.config.server.waittimes)).until(lambda driver:
            driver.find_element_by_xpath(
                                label_locator + '/following::select'))

        option_element = WebDriverWait(
            select_element, int(self.config.server.waittimes)).until(
            lambda driver: driver.find_element_by_xpath(
                CL.option_xpath %option))

        option_element.click()

    def _wait_element_by_text(self, text, position = ''):

        def web_drivers_find(driver):
            result = []
            locators= filter(lambda locator:
                locator.endswith('_xpath'), dir(CL))

            for locator in locators:
                if not position:
                    locator = getattr(CL, locator) %text
                    try:
                        result += driver.find_elements_by_xpath(locator)
                    except:
                        continue

                '''
                else:
                    locator = map(
                        lambda pos:getattr(CL, locator) %text + pos,
                            position %self.PAGEELEMENTS.itervalues())

                    for one_pos in locator:
                        try:
                            result += driver.find_elements_by_xpath(
                                locator + one_pos)
                        except:
                            continue
                '''

            # link text is easier if not use xpath
            # TODO: add position in link
            try:
                result += driver.find_elements_by_link_text(text)
            except:
                pass
            return result
        return web_drivers_find

    def click_by_text(self, text, index = 0):
        click_elements = WebDriverWait(
            self.driver, int(self.config.server.waittimes)).until(
                self._wait_element_by_text(text))
        click_elements[index].click()

    def verify_texts(self, find_targets):
        # find_targets can be a list to verify
        result = False
        for text in find_targets:
            result = result and self.verify_text(text)
        return result

    def verify_text(self, find_target):
        time.sleep(5)
        return find_target in self.driver.page_source
