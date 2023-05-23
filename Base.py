import yaml
from selenium import webdriver
import os

from selenium.webdriver.chrome.options import Options


class Base():
    set_key = None
    set_value = None
    def __init__(self,set_key,set_value):
        self.set_key = set_key
        self.set_value = set_value

    # @property
    def readYaml(self):
        filePath = os.path.dirname(__file__)
        print(filePath)
        fileNamePath = os.path.split(os.path.realpath(__file__))[0]
        yamlPath = os.path.join(fileNamePath,'env.yaml')
        # return self.yamlPath
        # print(self.yamlPath)
        with open(yamlPath, 'r',encoding='utf-8') as file:
            data = file.read()
            basic = yaml.safe_load(data)
            try:
                if self.set_key in basic.keys():
                    return basic[self.set_key][self.set_value]
                else:
                    print(f"self.set_key: {self.set_key}不存在")
            except Exception as e:
                print(f"key值{e}不存在")
            return basic

    def driver(self):
        if 'firefox' in Base('browser','driver').readYaml():
            self.driver = webdriver.Firefox()
        elif 'chrome' in Base('browser','driver').readYaml():
            self.driver = webdriver.Chrome()
        else:
            pass
        return self.driver

    def url(self):
        if 'test' in Base('address','url').readYaml():
            self.url = "http://test1.xcmg.com/cv3/login/login"
            # return self.url
        elif 'uat' in Base('address','url').readYaml():
            self.url = "http://58.218.196.216:11080/cv3/login/login"
            # return self.url
        else:
            pass
        return self.url

    def setup(self):
        chrome_options = Options()
        # 和浏览器打开的调试端口进行通信，浏览器使用chrome --remote-debugging-port=9222 开启调试
        chrome_options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=chrome_options)
        # self.driver = Base.driver(Base)
        # self.url = Base.url(Base)
        # self.driver.maximize_window()
        self.driver.get(Base.url(Base))
        self.driver.refresh()
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()

# if __name__ == '__main__':
#     Base.setup(Base)
#     Base.teardown(Base)


