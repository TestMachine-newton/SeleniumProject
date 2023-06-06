import random
import time

from selenium.webdriver.common.by import By
from Base import Base
from login import Login


class SignContract(Base):

    #经办签发条
    def signContract_Operator(self):
        #点击融票导航按钮
        self.driver.find_element(By.LINK_TEXT,"融票").click()
        #点击去签发按钮
        self.driver.find_element(By.CSS_SELECTOR,'.fr.ivu-btn.ivu-btn-primary').click()
        #点击单笔签发按钮
        self.driver.find_element(By.CSS_SELECTOR,'#BTN0049').click()
        #点击供应商选择框
        self.driver.find_element(By.CSS_SELECTOR,'[placeholder="请选择供应商"]').click()
        #再下拉框中选择供应商
        self.driver.find_element(By.XPATH,'//li[text()="万华实业集团有限公司"]').click()
        #输入金额
        self.driver.find_element(By.CSS_SELECTOR,'[placeholder="请输入融票金额，最多为14位整数2位小数"]').send_keys(random.randint(5000,10000))
        #点击日期选择框
        js = """document.querySelector('[placeholder="请选择承诺付款日期"]').removeAttribute('autocomplete')"""
        self.driver.execute_script(js)
        self.driver.find_element(By.CSS_SELECTOR, '[placeholder="请选择承诺付款日期"]').send_keys('2023-07-10')
        #点击信息输入页面的确定按钮
        self.driver.find_element(By.XPATH,'//span[text()="确认"]').click()
        #点击提示框的确定按钮
        time.sleep(2)
        # self.driver.find_element(By.XPATH,'(//span[text()="确认"])[2]').click()
        self.driver.find_element(By.CSS_SELECTOR, '.modal-footer span').click()
        #选择签发的第一条数据
        self.driver.find_element(By.XPATH,'(//*[@class="ivu-checkbox-input"])[2]').click()
        #下页面滚动条
        self.driver.execute_script("window.scrollTo(0,769)")
        #经办点击提交审核按钮
        self.driver.find_element(By.XPATH,'//span[text()="提交审核"]').click()
        #弹出提示弹窗，点击确定
        self.driver.find_element(By.XPATH,'(//span[text()="确定"])[2]').click()
        # self.driver.close()
        # self.driver.quit()


    def signContract_Executive(self):
        # 点击融票导航按钮
        self.driver.find_element(By.LINK_TEXT, "融票").click()
        #点击去审核
        self.driver.find_element(By.XPATH, '//span[text()="去审核"]').click()
        # 选择签发待审核的第一条数据
        self.driver.find_element(By.XPATH, '(//*[@class="ivu-checkbox-input"])[2]').click()
        #下页面滚动条
        self.driver.execute_script("window.scrollTo(0,769)")
        # 主管点击审核通过按钮
        self.driver.find_element(By.XPATH, '//span[text()="审核通过"]').click()
        # 点击审核通过后的弹窗上的确定按钮
        self.driver.find_element(By.XPATH,'//*[@class="ivu-modal-body"]//span[text()="确定"]').click()

if __name__ == '__main__':
    # Login('core', 'core_operator', 'core_operator_password').login()
    # for i in range(5):
    #     SignContract.signContract_Operator(SignContract)
    #
    Login('core', 'core_executive', 'core_executive_password').login()
    for i in range(5):
        SignContract.signContract_Executive(SignContract)