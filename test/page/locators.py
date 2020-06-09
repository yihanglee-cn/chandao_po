# 将所有元素定位信息，按不同的页面保存在不同的class下面
from selenium.webdriver.common.by import By

class LoginPageLocators():
    UserName = (By.ID, "account")
    PassWord = (By.NAME, "password")
    LoginSubmit = (By.ID, "submit")
    LoginName = (By.CLASS_NAME, "user-name")