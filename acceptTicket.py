# -*- coding: utf-8 -*-
# @Author: qinyue
# @Time: 2023/5/19 10:51
# @File: acceptTicket.py
import os
import time
import random

from selenium.webdriver.common.by import By
import datetime
import uuid

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Base import Base
from login import Login


class acceptTicket(Base):

    def acceptTicket(self):
        # 点击融票导航按钮
        self.driver.find_element(By.LINK_TEXT, "融票").click()
        #点击发起融资/转让tab页第一条数据的去签约按钮
        self.driver.find_element(By.XPATH,'(//span[text()="去融资"])[1]').click()
        #点击融资申请资金方选择列表中第一个资金方
        self.driver.find_element(By.XPATH,'(//span[text()="选择"])[1]').click()
        # 下页面滚动条
        self.driver.execute_script("window.scrollTo(0,300)")
        time.sleep(1)
        #点击下一步
        #self.driver.find_element(By.CSS_SELECTOR,'button:nth-child(2)').click()
        self.driver.find_element(By.XPATH, '//span[text()="下一步"]').click()
        #选择第一个收款账户
        self.driver.find_element(By.XPATH,'(//input[@type="radio"])[1]').click()
        #self.driver.find_element(By.CSS_SELECTOR,'label:nth-child(1) input').click()
        #点击提交申请按钮
        self.driver.find_element(By.XPATH,'//span[text()="提交申请"]').click()
        #self.driver.find_element(By.CSS_SELECTOR,'button:nth-child(2)').click()
        # 点击线上提交材料
        time.sleep(1)
        # preserve_button = self.driver.find_element(By.XPATH, '//span[text()="线上提交材料"]')
        # WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(preserve_button))
        self.driver.find_element(By.XPATH, '//span[text()="线上提交材料"]').click()
        #self.driver.find_element(By.CSS_SELECTOR, 'button:nth-child(2)').click()
        #关闭下载融资资料清单的弹窗
        preserve_button = self.driver.find_element(By.CSS_SELECTOR, '.modal-footer button:nth-child(2)')
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(preserve_button))
        #self.driver.find_element(By.XPATH,'(//*[@class="modal-wrapper"]//span[text()="关闭"])').click()
        self.driver.find_element(By.CSS_SELECTOR,'.modal-footer button:nth-child(2)').click()
        #点击添加新合同按钮
        self.driver.find_element(By.CSS_SELECTOR, 'button:nth-child(2)').click()
        #输入合同编号
        self.driver.find_element(By.CSS_SELECTOR,'[placeholder="请输入与供应商签订的合同编号，支持自定义编号"]').send_keys(random.randint(222222222222,888888888888))
        # 输入合同名称
        self.driver.find_element(By.CSS_SELECTOR, '[placeholder="请输入合同名称"]').send_keys('qinyue_ceshi')
        # 点击输入合同签署日期选择框
        js = """document.querySelector('[placeholder="请选择合同签署日期"]').removeAttribute('autocomplete')"""
        self.driver.execute_script(js)
        self.driver.find_element(By.CSS_SELECTOR, '[placeholder="请选择合同签署日期"]').send_keys(datetime.datetime.now().strftime('%Y-%m-%d'))
        # 输入合同金额
        self.driver.find_element(By.CSS_SELECTOR, '[placeholder="请输入合同金额"]').send_keys('100000')
        # 点击上传合同附件
        self.driver.find_element(By.XPATH, '//span[text()="点击上传"]').click()
        os.system(r"C:\MyPython\upload.exe")
        preserve_button = self.driver.find_element(By.XPATH, '(//*[@class="operator"])[1]')
        WebDriverWait(self.driver,5).until(expected_conditions.element_to_be_clickable(preserve_button))
        # 点击商务合同添加页面右下角保存按钮
        self.driver.find_element(By.XPATH, '//span[text()="保存"]').click()
        #点击下一步去上传发票
        self.driver.find_element(By.XPATH,'//*[@class="table-bottom text-center"]/button[2]').click()




if __name__ == '__main__':
    Login('corp', 'corp_operator', 'corp_operator_password').login()
    acceptTicket.acceptTicket(acceptTicket)


