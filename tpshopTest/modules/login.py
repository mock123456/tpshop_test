import allure
import requests
from pip._internal.utils import urls

from Tools import Tool
from selenium import webdriver


@allure.epic('Tpshop')
@allure.feature('登录注册')
class Deng_lu():
    @staticmethod
    @allure.story('登录')
    def deng_lu():
        """执行登录操作，登录成功后返回当前页面的url以及对应的driver"""
        data = Tool.loadConfig()
        response = Tool.login(url='http://localhost/index.php/Home/user/login.html', username1=data['username'],
                              password1=data['password'])
        # url = response['url']
        driver = response['driver']
        # session = response['session']
        cookies = response['cookies']
        # return driver, session, url, cookies
        return cookies,driver
