from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_action import BaseAction


class MinePage(BaseAction):

    login_sign_up_button = By.XPATH, "//*[@text='登录/注册']"

    def click_login_sign_up(self):
        self.click(self.login_sign_up_button)

    def find_toast(driver, message, timeout=100):
        """
        # message: 预期要获取的toast的部分消息
        """
        message1 = By.XPATH, "//*[contains(@text,'" + message + "')]"  # 使用包含的方式定位

        element = WebDriverWait(driver, timeout, 0.1).until(lambda x: x.find_element(message1))
        return element.text