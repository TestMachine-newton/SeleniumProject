#encoding=utf-8
import time
from Base import Base
from selenium import webdriver
from selenium.webdriver.common.by import By

class login(Base):
    def login(self):
        Base.driver(Base)
        Base.setup(Base)
        corename = Base.readYaml(self,'env.yaml')['core'][0]['core']
        core_operator = Base.readYaml(self,'env.yaml')['core'][1]['core_operator']
        core_operator_password = Base.readYaml(self, 'env.yaml')['core'][2]['core_operator_password']
        # self.driver = webdriver.Chrome()
        self.driver.get("http://58.218.196.216:11080/cv3/login/login")
        self.driver.refresh()
        self.driver.maximize_window()
        self.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div[2]/div/div[1]/div[1]/div/form/div/ul/li[1]/div/span[2]/input").send_keys(corename)
        self.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div[2]/div/div[1]/div[1]/div/form/div/ul/li[2]/div/span[2]/input").send_keys(core_operator)
        self.driver.find_element(by=By.ID,value="password").send_keys(core_operator_password)
        self.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div[2]/div/div[1]/div[1]/div/form/div/ul/li[4]/div/div/span/input").send_keys("1234")
        self.driver.find_element(by=By.LINK_TEXT,value="获取验证码").click()
        time.sleep(10)
        self.driver.find_element(by=By.ID,value="loginSubmit").click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
if __name__ == '__main__':
    login.login(login)