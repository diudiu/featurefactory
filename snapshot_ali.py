#! /usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# browser = webdriver.PhantomJS()
browser = webdriver.Chrome()
# browser.get("https://qiye.aliyun.com/")
# browser.get("https://mailsso.mxhichina.com/dingdinglogin/loginByDingQrCode.htm?app_code=smartmail&domain_name=qiye.aliyun.com&lang=zh_CN&redirect_url=https%3A%2F%2Fqiye.aliyun.com%2Falimail%2Fauth%2FcallbackForCore%3Freurl%3D%252Falimail%252F&sign=e36891af22c5deea564e239108a8280b")
browser.get("https://mailsso.mxhichina.com/login.htm?app_code=smartmail&lang=zh_CN&redirect_url=https://qiye.aliyun.com/alimail/auth/callbackForCore?reurl=%2Falimail%2F&sign=e36891af22c5deea564e239108a8280b&device_id=230fc99d87c44393a7a6b5dd7eae7bbf")

try:
    email = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
        # EC.presence_of_element_located((By.ID, "ding-login-iframe"))
    )
    email.send_keys("develop@yiduilu.com")

    password = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    password.send_keys("Syph123!")

    submit = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "login_submit_btn"))
    )
    # submit.click()

finally:
    pass

# email = browser.find_element_by_id("username")
# email.send_keys("develop@yiduilu.com")
#
# # password = browser.find_element_by_class_name("password")
# password = browser.find_element_by_id("password")
# password.send_keys("Syph123!")
# email.send_keys("Syph123!")

#
# submit = browser.find_element_by_id("login_submit_btn")
# submit.click()
# #
# # time.sleep(1)
# # browser.switch_to.window(browser.window_handles[0])
#
# inbox = browser.find_element_by_xpath("//span[@title='收件箱']")
# inbox.click()
#
# time.sleep(1)
# firstMail = browser.find_element_by_xpath("//div[@sign='start-from']")
# firstMail.click()
#
# browser.save_screenshot("test163.png")
# browser.close()
# browser.quit()

