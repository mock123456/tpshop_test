from selenium import  webdriver
from Tools import Tools

class registration:
    def __init__(self ,account ,password):
        self.account = account
        self.password = password

    def chPage(self):
        """切换到注册页面"""

    def test_registration(self):
        service = Tools.login()
        session = service['session_id']
        url = service['url']
