import time
from selenium.webdriver.chrome.service import Service
import pytest
import pytest_ordering
from selenium import webdriver

import Tools
from Tools import Tool
from modules import login


# @pytest.mark.run(order=1)
# def test_001():
#     """判断有没有跳转到主页"""
#     url, driver = login.Deng_lu.deng_lu()
#     driver.get(driver.current_url)
#     assert driver.current_url == "http://localhost/index.php/Home/User/index.html"


# cookies, driver = login.Deng_lu.deng_lu()
# driver.quit()

print('正在使用cookies重连网络')
driver = webdriver.Chrome(service=Service(r'E:\浏览器下载\chromedriver-win64\chromedriver.exe'))
driver.maximize_window()
driver.implicitly_wait(30)
time.sleep(30)
data = Tools.Tool.loadConfig('./config/session.json')
print(data)
cookies = data['cookies']
driver.get('http://localhost/index.php/Home/User/index.html')
for cookie in cookies:
    driver.add_cookie(cookie)
driver.get('http://localhost/index.php/Home/User/index.html')
driver.refresh()
input('输入以结束')