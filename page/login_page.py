from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_action import BaseAction


class LoginPage(BaseAction):

    # 用户名
    username_edit_text = By.ID, "com.tpshop.malls:id/edit_phone_num"

    # 密码
    password_edit_text = By.ID, "com.tpshop.malls:id/edit_password"

    # 登录
    login_button = By.ID, "com.tpshop.malls:id/btn_login"



    def input_username(self, username):
        self.input(self.username_edit_text, username)

    def input_password(self, password):
        self.input(self.password_edit_text, password)

    def click_login(self):
        self.click(self.login_button)

    def is_toast_exist(self, message):
        self.is_toast_exist(message)

