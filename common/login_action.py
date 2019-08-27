from common.disire_caps import disereDemo
from common.commomFunction import Common
import logging
from selenium.webdriver.common.by import By
import yaml
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction

with open('../config/capability.yaml', 'r', encoding='utf-8') as file:
    Data=yaml.load(file)

class LoginView(Common):

    username = (By.ID,'cn.victorplus.car:id/job_number_et')
    phonenum = (By.ID,'cn.victorplus.car:id/et_account')
    assertnum = (By.ID,'cn.victorplus.car:id/et_password')
    environment = (By.ID,'cn.victorplus.car:id/sp_url_choice')
    environment_DEV = (By.XPATH,'//*[@text="DEV"]')
    environment_t1 = (By.XPATH,'//*[@text="T"]')
    environment_t2 = (By.XPATH,'//*[@text="T2"]')
    environment_t3 = (By.XPATH,'//*[@text="T3"]')
    loginBtn = (By.ID,'cn.victorplus.car:id/btn_login')
    head_picture = (By.ID,'cn.victorplus.car:id/iv_head')

    def loginaction(self):
        self.yunxuclick()
        self.yunxutwo()

        logging.info('======start login=========')
        logging.info('输入工号')
        self.driver.find_element(*self.username).send_keys(Data['jobNum'])

        logging.info('输入手机号码后四位')
        self.driver.find_element(*self.phonenum).send_keys(Data['phone'])

        logging.info('输入验证码')
        self.driver.find_element(*self.assertnum).send_keys(Data['Vernum'])

        self.driver.find_element(*self.environment).click()

        logging.info('选择环境')
        self.driver.find_element(*self.environment_t1).click()

        logging.info('click loginBtn')
        self.driver.find_element(*self.loginBtn).click()
        logging.info('========stop  login=========')

        WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_id('cn.victorplus.car:id/gesture_view'))
        for i in range(2):
            logging.info('开始九宫格 第%s次，，，，，'%(i+1))
            TouchAction(self.driver).press(x=251, y=832).wait(100) \
                .move_to(x=541, y=832).wait(100) \
                .move_to(x=835, y=832).wait(100) \
                .move_to(x=835, y=1119).wait(100) \
                .move_to(x=835, y=1411).wait(200).release().perform()
        logging.info('九宫格设置结束，，，，，')


if __name__ == '__main__':
    driver = disereDemo()
    loginDemo = LoginView(driver)
    loginDemo.loginaction()




