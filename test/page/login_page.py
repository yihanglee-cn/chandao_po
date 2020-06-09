from selenium import webdriver
from time import sleep
from .locators import LoginPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def wait(self, element):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(element))
        except Exception:
            print("Waiting {}... ...".format(element))

class LoginPage(BasePage):
    """登录页面"""
    def enter_username(self):
        BasePage.wait(*LoginPageLocators.UserName)
        ele = self.driver.find_element(*LoginPageLocators.UserName)
        ele.send_keys("admin")

    def enter_password(self):
        BasePage.wait(*LoginPageLocators.PassWord)
        ele = self.driver.find_element(*LoginPageLocators.PassWord)
        ele.send_keys("123456")

    def click_login(self):
        BasePage.wait(*LoginPageLocators.LoginSubmit)
        ele = self.driver.find_element(*LoginPageLocators.LoginSubmit)
        ele.click()

    def check_username(self):
        BasePage.wait(*LoginPageLocators.LoginName)
        ele = self.driver.find_element(*LoginPageLocators.LoginName)
        return ele.text



