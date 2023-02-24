#encoding=utf-8
import time
from Base import Base
from selenium.webdriver.common.by import By

class Login(Base):
    Base.setup(Base)
    def __init__(self,name,operator,passeord):
        self.name = Base(name,name).readYaml()
        self.operator = Base(name,operator).readYaml()
        self.passeord = Base(name,passeord).readYaml()
    def login(self):
        self.driver.find_element(By.CSS_SELECTOR, '[placeholder="请输入企业全称"]').send_keys(self.name)
        self.driver.find_element(By.NAME,'mobile').send_keys(self.operator)
        self.driver.find_element(By.ID,'password').send_keys(self.passeord)
        self.driver.find_element(By.NAME, "smsVerifyCode").send_keys("1234")
        self.driver.find_element(By.LINK_TEXT,'获取验证码').click()
        time.sleep(10)
        self.driver.find_element(By.ID,'loginSubmit').click()
        # cookies = self.driver.get_cookies()
        # print(self.driver.current_window_handle)
        # print(self.driver.window_handles)
        # print(cookies)
#
# if __name__ == '__main__':
#     Login('core','core_operator','core_operator_password').login()
