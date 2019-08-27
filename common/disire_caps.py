from appium import webdriver
import yaml
import logging
import logging.config
import os

conf_log='../config/log.conf'
logging.config.fileConfig(conf_log)
logging=logging.getLogger()

def disereDemo():
    with open('../config/capability.yaml','r',encoding='utf-8') as file:
        Data=yaml.load(file)

    base_dir = os.path.dirname((os.path.dirname(__file__)))
    app_dir = os.path.join(base_dir, 'app', Data['appName'])    #os.path.join()将几个路径拼接起来

    desired_caps={}
    desired_caps['platformName']=Data['platformName']
    desired_caps['deviceName']=Data['deviceName']
    desired_caps['platformVersion']=Data['platformVersion']
    desired_caps['appPackage']=Data['appPackage']
    desired_caps['appActivity']=Data['appActivity']
    desired_caps['app']=app_dir
    desired_caps['unicodeKeyboard']=Data['unicodeKeyboard']
    desired_caps['resetKeyboard']=Data['resetKeyboard']
    desired_caps['noReset']='True'
    desired_caps['automationName']='uiautomator2'


    driver=webdriver.Remote('http://'+str(Data['ip'])+':'+str(Data['port'])+'/wd/hub',desired_caps)
    driver.implicitly_wait(8)#等待8秒
    logging.info('启动成功')
    return driver

if __name__ == '__main__':
    disereDemo()
    # with open('../config/capability.yaml','r',encoding='utf-8') as file:
    #     Data=yaml.load(file)
    # print(os.path.dirname((os.path.dirname(__file__))))
    # base_dir=os.path.dirname((os.path.dirname(__file__)))
    # app_dir=os.path.join(base_dir,'app',Data['appName'])
    # print(app_dir)