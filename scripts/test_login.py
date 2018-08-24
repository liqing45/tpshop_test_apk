import pytest
from selenium.webdriver.support.wait import WebDriverWait

from base.base_driver import init_driver
from page.page import Page


class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)



    def test_login(self):
        self.page.home.click_mine()

        self.page.mine.click_login_sign_up()
        self.page.mine.find_toast("请先")
        # self.page.login.find_toast("请先")
        self.page.login.input_username("13800138006")
        self.page.login.input_password("123456")
        self.page.login.click_login()
        self.page.login.find_toast("登录成功")
