from common.login_action import LoginView
import logging,time
from common.disire_caps import disereDemo
from selenium.webdriver.common.by import By
import yaml
from selenium.webdriver.support.ui import WebDriverWait

with open('../config/capability.yaml', 'r', encoding='utf-8') as file:
    Data = yaml.load(file)

class Zhengxing(LoginView):
    new_order=(By.ID,'cn.victorplus.car:id/btn_new_order')
    zhengxingtitle=(By.XPATH,'//*[@text="征信"]')
    # 商家信息
    order_marketName=(By.ID,'cn.victorplus.car:id/iv_market_name_next')      #市场
    order_marketChooseName=(By.XPATH,'//*[@text="鸿源二手车市场"]')
    order_CarDealerStore=(By.ID,'cn.victorplus.car:id/iv_dealer_name_next')  #车商门店
    order_CarDealerStoreNmae = (By.XPATH, '//*[@text="迟哥哥第一门店"]')
    #主贷人
    PrincipalLender_name=(By.ID,'cn.victorplus.car:id/et_name')              #主贷人姓名
    PrincipalLender_idCard=(By.ID,'cn.victorplus.car:id/et_idcard')          #主贷人身份证
    PrincipalLender_phone=(By.ID,'cn.victorplus.car:id/et_phone')            #主贷人手机
    VerificationCode=(By.ID,'cn.victorplus.car:id/et_get_code')              #验证码
    #配偶
    spouse_MaritalStatus=(By.ID,'cn.victorplus.car:id/iv_next18')            #配偶婚姻状况
    spouse_weihun=(By.XPATH,'//*[@text="未婚"]')                             #配偶婚姻状况
    spouse_yihun=(By.XPATH, '//*[@text="已婚"]')
    spouse_liyi=(By.XPATH, '//*[@text="离异"]')
    spouse_sangou=(By.XPATH, '//*[@text="丧偶"]')
    pouse_name=(By.ID,'cn.victorplus.car:id/et_mate_name_data')                                 #配偶姓名
    pouse_idcard=(By.ID,'cn.victorplus.car:id/et_mate_card_data')                               #配偶身份证
    pouse_idcard_validTime=(By.ID,'ccn.victorplus.car:id/tv_mate_card_date_data')               #配偶身份证有效期
    pouse_idcard_validTime_confirmBtn=(By.XPATH,'//*[@text="确定"]')
    pouse_phone=(By.ID,'cn.victorplus.car:id/et_mate_phone_num_data')                           #配偶手机号
    #授权
    shouquan=(By.ID,'cn.victorplus.car:id/iv_power_idcard')
    shouquan_pictureId=(By.ID,'cn.victorplus.car:id/cb_check')
    shangchuanBtn=(By.ID,'cn.victorplus.car:id/tv_save')
    #提交按钮
    zhengxingsubmitBtn=(By.ID,'cn.victorplus.car:id/tv_commit')
    zhengxingsubmitBtnConfirm=(By.ID,'android:id/button1')
    #返回
    goBackBtn=(By.ID,'cn.victorplus.car:id/iv_back')
    #授权
    shouquanBtn=(By.XPATH,'//*[@text="授权"]')
    orderGuanli=(By.XPATH,'//*[@text="订单管理"]')

    def inputZhengXin(self):

        loginDemo = LoginView(self.driver)
        loginDemo.loginaction()

        WebDriverWait(self.driver,8).until(lambda x:x.find_element(*self.new_order))
        logging.info('点击新建订单')
        self.driver.find_element(*self.new_order).click()
        WebDriverWait(self.driver, 8).until(lambda x: x.find_element(*self.zhengxingtitle))
        logging.info('开始选择市场名称')
        self.driver.find_element(*self.order_marketName).click()
        self.driver.find_element(*self.order_marketChooseName).click()
        logging.info('开始选择车商门店')
        self.driver.find_element(*self.order_CarDealerStore).click()
        self.driver.find_element(*self.order_CarDealerStoreNmae).click()
        logging.info('开始录入主贷人信息')
        self.driver.find_element(*self.PrincipalLender_name).send_keys(Data['zhudainame'])
        self.driver.find_element(*self.PrincipalLender_idCard).send_keys(Data['zhudaiidcard'])
        self.driver.find_element(*self.PrincipalLender_phone).send_keys(Data['zhudaiiphone'])
        self.driver.find_element(*self.VerificationCode).send_keys(Data['certnum'])
        logging.info('选择主贷人婚姻状况')
        self.driver.find_element(*self.spouse_MaritalStatus).click()
        self.driver.find_element(*self.spouse_weihun).click()

        logging.info('向上滑动')
        self.swipeAct(0.5, 0.9, 0.5, 0.4,1000)

        logging.info('上传电子信息授权书')
        self.driver.find_element(*self.shouquan).click()
        self.driver.find_elements(*self.shouquan_pictureId)[0].click()
        self.driver.find_element(*self.shangchuanBtn).click()

        WebDriverWait(self.driver, 8).until(lambda x: x.find_element(*self.shouquanBtn))
        logging.info('向下滑动')
        self.swipeAct(0.5, 0.3, 0.5, 0.6,1000)
        self.driver.find_element(*self.zhengxingsubmitBtn).click()
        self.driver.find_element(*self.zhengxingsubmitBtnConfirm).click()
        time.sleep(5)
        self.getScreenShot('征信信息录入成功')





if __name__ == '__main__':
    driver = disereDemo()
    zhengxingDemo = Zhengxing(driver)
    zhengxingDemo.inputZhengXin()





