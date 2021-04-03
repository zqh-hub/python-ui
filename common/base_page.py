from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from common import dir_config
import time
from common.log import MyLog


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.my_log = MyLog()
        # self.driver = webdriver.Chrome()

    def wait_presence_return_bool(self, ele_loc, wait_time=10, poll_frequency=0.5, doc=""):
        try:
            WebDriverWait(self.driver, wait_time, poll_frequency).until(ec.visibility_of_element_located(ele_loc))
            self.my_log.loging("找到元素{0}出现".format(ele_loc), "INFO")
            return True
        except:
            self.my_log.loging("未找到元素{0}出现".format(ele_loc), "ERROR")
            return False

    def wait_visible_return_ele(self, ele_loc, wait_time=10, poll_frequency=0.5, doc=""):
        self.my_log.loging("开始等待元素{0}出现".format(ele_loc), "INFO")
        try:
            WebDriverWait(self.driver, wait_time, poll_frequency).until(ec.visibility_of_element_located(ele_loc))
            self.my_log.loging("找到元素{0}出现".format(ele_loc), "INFO")
            return self.driver.find_element(*ele_loc)
        except:
            self.my_log.loging("未找到元素{0}出现".format(ele_loc), "ERROR")
            self.save_screen(doc)
            raise

    def click_ele(self, ele_loc, doc=""):
        ele = self.wait_visible_return_ele(ele_loc, doc=doc)
        try:
            ele.click()
            self.my_log.loging("点击了元素{0}".format(ele_loc), "INFO")
        except:
            self.my_log.loging("未点击到元素{0}".format(ele_loc), "ERROR")
            self.save_screen(doc)
            raise

    def ele_input_key(self, ele_loc, value, doc=""):
        ele = self.wait_visible_return_ele(ele_loc, doc=doc)
        try:
            ele.send_keys(value)
            self.my_log.loging("向{0}输入文本成功".format(ele_loc), "INFO")
        except:
            self.my_log.loging("向{0}输入文本失败".format(ele_loc), "ERROR")
            self.save_screen(doc)
            raise

    def get_text(self, ele_loc, doc=""):
        element = self.wait_visible_return_ele(ele_loc, doc=doc)
        try:
            value = element.text
            self.my_log.loging("获取{}的文本值成功".format(ele_loc), "INFO")
            return value
        except:
            self.my_log.loging("获取{}的文本值成功".format(ele_loc), "ERROR")
            self.save_screen(doc)
            raise

    def get_element_attribute(self, locator, attr, doc):
        element = self.wait_visible_return_ele(locator, doc=doc)
        try:
            value = element.get_attribute(attr)
            self.my_log.loging("获取元素{0}的{1}属性值成功".format(locator, attr), "INFO")
            return value
        except:
            self.my_log.loging("获取元素{0}的{1}属性值失败".format(locator, attr), "ERROR")
            self.save_screen(doc)
            raise

    def save_screen(self, doc):
        # 图片的名称：模块名_页面名称_操作名称_年-月-日_时分秒.png
        file_path = dir_config.screen_dir
        shot_time = time.strftime("%Y-%m-%d %H:%M:%s", time.localtime(time.time()))
        file_name = "{0}_{1}.png".format(doc, shot_time)
        print(file_path + file_name)
        self.driver.save_screenshot(file_path + file_name)
