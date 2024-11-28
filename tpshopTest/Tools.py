import json
import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common import desired_capabilities
from PIL import Image
from retry import retry
import Ocr


class Tool:
    """这是一个工具类，主要存放了selenium自动化的接口"""
    def __init__(self):
        """初始化登录"""
        self.driver = self.initialize()

    def initialize(self):
        driver = webdriver.Chrome(service=Service(r'E:\浏览器下载\chromedriver-win64\chromedriver.exe'))
        driver.maximize_window()
        driver.implicitly_wait(30)
        return driver


    def __repr__(self):
        print("这是一个提供工具的类，主要存放了selenium自动化的接口")

    @staticmethod
    @retry(Exception, tries=5, delay=1)
    def login(url, username1, password1):
        """自动化登录操作，输入url,账号和密码，获取当前登录状态，返回包含session_id和url的dict对象，retry装饰器用来设置重试次数
        input: url,username1,password1
        return:  {"driver": driver, "session": session_id, "url": remote_url, "cookies": cookies}
        """
        options = webdriver.ChromeOptions()
        # options.add_experimental_option('detach', True)
        driver = webdriver.Chrome(service=Service(r'E:\浏览器下载\chromedriver-win64\chromedriver.exe'), options=options)
        driver.maximize_window()
        driver.implicitly_wait(30)
        tool = Tool()
        driver = tool.driver
        driver.get(url)
        # 截取验证码图片,调用接口编码为Base64格式
        driver.save_screenshot('./src/login.png')
        element_checkCum = driver.find_element(By.CSS_SELECTOR, '.check_cum_img img')
        location = element_checkCum.location
        size = element_checkCum.size
        # 进一步截取验证码图片,保存为picture，保存为jpg格式
        i = Image.open('./src/login.png')
        picture = i.crop((location['x'], location['y'], location['x'] + size['width'], location['y'] + size['height']))
        picture.save('./src/login1.png')
        response = Ocr.verification_code(picture_url='./src/login1.png')
        data = json.loads(response)
        words_dict = data['words_result'][0]
        code = words_dict['words']
        print(code)
        username = driver.find_element(By.CSS_SELECTOR, '[placeholder="手机号/邮箱"]')
        password = driver.find_element(By.CSS_SELECTOR, '[placeholder="密码"]')
        check_code = driver.find_element(By.CSS_SELECTOR, '[placeholder="验证码"]')
        login_button = driver.find_element(By.XPATH, '//a[@class="J-login-submit"]')
        try:
            # 判断有没有提示框
            # username.send_keys('17683700412')
            username.send_keys(username1)
            time.sleep(5)
            # password.send_keys('kx135549')
            password.send_keys(password1)
            time.sleep(5)
            check_code.send_keys(code)
            time.sleep(2)
            login_button.click()
            # 寻找错误提示框，没找到提示框，出现异常那么就是正常登录了，执行except语句；如果找到了那就退出界面，重新尝试登录
            prompt = driver.find_element(By.CSS_SELECTOR, ".layui-layer-content.layui-layer-padding")
            print("验证码错误,正在重新启动")
            driver.quit()
            # assert 抛出异常，重启
            assert 0
        except NoSuchElementException:
            # 获取session_id和服务器的url,写入json到config.json中
            print("登录成功")
            session_id = driver.session_id
            remote_url = driver.command_executor._url
            cookies = driver.get_cookies()
            # print({"session": session_id, "url": remote_url}, "cookies": cookies)
            Tool.updateConfig({"session": session_id, "url": remote_url, "cookies": cookies})
            return {"driver": driver, "session": session_id, "url": remote_url, "cookies": cookies}
        # finally:
        #     driver.close()
        # 当出现提示框时,提取提示框信息并且打印出来,如验证码错误、账号错误、密码错误,这个功能暂时不需要，优先保证能登录就行了
        # except NoSuchElementException:
        #     prompt = driver.find_element(By.CSS_SELECTOR, ".layui-layer-content.layui-layer-padding")
        #     print(prompt.text)
        # finally:
        #     prompt = driver.find_element(By.CSS_SELECTOR, ".layui-layer-content.layui-layer-padding")
        #     print(prompt.text)


        # main_page = driver.find_element(By.XPATH, '//a[contains(text(), "首页")]').click()
        # phone_page = driver.find_element(By.XPATH, '//a[contains(text(), "手机城")]').click()
        # phone_cart = driver.find_elements(By.CSS_SELECTOR, '.shop-list-tour.ma-to-20.p .shop-list-splb.p ul .p-btn a ')
        # list1 = []
        # for phone in phone_cart:
        #     list1.append(phone)
        # list1[1].click()eg
        #
        # input('输入以结束')

    @staticmethod
    def loadConfig(file='./config/config.json'):
        """加载配置文件信息"""
        with open(file, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
            return json_data

    @staticmethod
    def updateConfig(data, file='./config/session.json'):
        """更新配置信息并保存"""
        with open(file, 'r+', encoding='utf-8') as f:
            json.dump(data, f)

    @staticmethod
    def driver(data):
        url = data['url']
        session_id = data['session']
        options = webdriver.ChromeOptions()
        driver = webdriver.Remote(command_executor=url, options=options)
        driver.session_id = session_id
        print(driver)
        return driver

