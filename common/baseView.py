class BaseView(object):
    def __init__(self,driver):
        self.driver=driver

    def find_element(self, *args):
        return self.driver.find_element(*args)

    def find_elements(self,*args):
        return self.driver.find_elements(*args)

    def get_window_size(self):
        return self.driver.get_window_size()

    def swipe(self,start_x,start_y,end_x,end_y,duration):
        return self.driver.swipe(self,start_x,start_y,end_x,end_y,duration)
