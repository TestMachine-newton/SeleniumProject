import time

from selenium.webdriver.common.by import By
from Base import Base
from login import login



class signContract(Base):
    #经办签发条
    def signContract(self):
        # Base.driver(Base)
        # print(self.driver)
        # self.driver.implicitly_wait(5)
        # print(self.driver.current_window_handle)
        # print(self.driver.window_handles)
        #点击融票导航按钮
        self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div/div[1]/div[1]/div[2]/ul/a[1]').click()
        #点击去签发按钮
        self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div/div[2]/div/div[3]/div/div[2]/div/div/div[1]/div[1]/div/h3/button[2]').click()
        #点击单笔签发按钮
        self.driver.find_element(by=By.ID,value='BTN0049').click()
        #点击供应商选择框
        self.driver.find_element(by=By.XPATH,value='/html/body/div[4]/div[2]/div/div/div[2]/form/div/div/div[2]/div/div/div[1]/div/input').click()
        #再下拉框中选择供应商
        self.driver.find_element(by=By.XPATH,value='/html/body/div[4]/div[2]/div/div/div[2]/form/div/div/div[2]/div/div/div[2]/ul[2]/li[6]').click()
        #输入金额
        self.driver.find_element(by=By.XPATH,value='/html/body/div[4]/div[2]/div/div/div[2]/form/div/div/div[3]/div/div/div[2]/input').send_keys('5000')
        #点击日期选择框
        self.driver.find_element(by=By.XPATH,value='/html/body/div[4]/div[2]/div/div/div[2]/form/div/div/div[4]/div/div[1]/div[1]/div/div/input').click()
        #点击日期选择框右翻页按钮
        self.driver.find_element(by=By.XPATH,value='/html/body/div[4]/div[2]/div/div/div[2]/form/div/div/div[4]/div/div[1]/div[2]/div/div/div/div[1]/span[5]').click()
        #选择日期
        self.driver.find_element(by=By.XPATH,value='/html/body/div[4]/div[2]/div/div/div[2]/form/div/div/div[4]/div/div[1]/div[2]/div/div/div/div[2]/div/span[25]/em').click()
        #点击信息输入页面的确定按钮
        self.driver.find_element(by=By.XPATH,value='/html/body/div[4]/div[2]/div/div/div[3]/div/button[1]').click()
        #点击提示框的确定按钮
        self.driver.find_element(by=By.XPATH,value='/html/body/div[8]/div/div/div[2]/div/button').click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)

if __name__ == '__main__':
    login.login(login)
    signContract.signContract(signContract)