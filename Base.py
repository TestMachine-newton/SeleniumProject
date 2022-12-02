import yaml
from selenium import webdriver
import os


class Base():

    def readYaml(self,filename):
        self.filePath = os.path.dirname(__file__)
        self.fileNamePath = os.path.split(os.path.realpath(__file__))[0]
        self.yamlPath = os.path.join(self.fileNamePath,filename)
        # return self.yamlPath
        with open(self.yamlPath, 'r',encoding='utf-8') as file:
            data = file.read()
            basic = yaml.safe_load(data)
            return basic

    def driver(self):
        self.driver = self.readYaml(self, 'env.yaml')['driver']
        # print(self.driver)
        # print(type(driver))
        if 'firefox' in self.driver:
            self.driver = webdriver.Firefox()
            # print('现在选择的是firefox')
        elif 'chrome' in self.driver:
            self.driver = webdriver.Chrome()
            # print('现在选择的是chrome')
        else:
            pass
        return self.driver
    def setup(self):
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()


if __name__ == '__main__':
    Base.driver(Base)
    Base.setup(Base)
    Base.teardown(Base)


