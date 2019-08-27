from common.disire_caps import disereDemo
from common.baseView import BaseView
import logging,time,os
from selenium.webdriver.common.by import By



class Common(BaseView):
    yunxuBtn=(By.ID,'com.android.packageinstaller:id/permission_allow_button')

    def yunxuclick(self):
        logging.info('========== start 1 ==========')
        try:
            yunxuEle = self.driver.find_element(*self.yunxuBtn)
        except Exception as e:
            logging.info('no such element:允许 one ')
        else:
            logging.info('click 允许 one')
            yunxuEle.click()
    def yunxutwo(self):
        logging.info('======== start 2 ========')
        try:
            yunxuEle = self.driver.find_element(*self.yunxuBtn)
        except Exception as e:
            logging.info('no such element:允许 two')
        else:
            logging.info('click 允许 two ')
            yunxuEle.click()

    def getSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    def swipeAct(self,a, b, c, d, t):
        x1 = int(self.getSize()[0] * a)
        x2 = int(self.getSize()[0] * c)
        y1 = int(self.getSize()[1] * b)
        y2 = int(self.getSize()[1] * d)
        self.driver.swipe(x1, y1, x1, y2, t)

    def getTime(self):
        self.now=time.strftime('%Y-%m-%d %H_%M_%S')
        return self.now

    def getScreenShot(self,module):
        time=self.getTime()
        image_file=os.path.dirname(os.path.dirname(__file__))+'/screenShots/%s_%s.png'%(module,time)
        logging.info('get %s screenShot'%module)
        self.driver.get_screenshot_as_file(image_file)




if __name__ == '__main__':
    driver = disereDemo()
    startup=Common(driver)
    startup.yunxuclick()
    startup.yunxutwo()