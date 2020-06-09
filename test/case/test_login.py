from selenium import webdriver
import unittest
from web_ui.chandao_po.test.page.login_page import LoginPage
import os
from web_ui.chandao_po.utils.parse_ini import ParseINI

class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        conf = ParseINI()
        current_path =
        print(current_path)
        conf.parse_ini()
        self.driver.get("http://www.chandao.com/zentaopms/www/index.php")

    def tearDown(self):
        # sleep(2)
        self.driver.quit()

    def test_01_login_success(self):
        """用户名密码正确，登录成功"""
        loginpage = LoginPage(self.driver)
        # # self.driver.find_element_by_id("account").send_keys("admin")
        # self.driver.find_element(*LoginPageLocators.UserName).send_keys("admin")
        # # self.driver.find_element_by_name("password").send_keys("123456")
        # self.driver.find_element(*LoginPageLocators.PassWord).send_keys("123456")
        # # self.driver.find_element_by_id("submit").click()
        # self.driver.find_element(*LoginPageLocators.LoginSubmit).click()
        # # sleep(0.5)
        # ele = self.driver.find_element(*LoginPageLocators.LoginName).text
        # self.assertEqual("admin", ele)
        loginpage.enter_username()
        loginpage.enter_password()
        loginpage.click_login()
        loginpage.check_username()
        # 1

if __name__ == "__main__()":
    unittest.main()
