import unittest
from common import disire_caps
import logging
import time



class TestBase(unittest.TestCase):
    def setUp(self):
        logging.info('=======setUp========')
        self.driver = disereDemo()

    def tearDown(self):
        logging.info('=======tearDown========')
        time.sleep(5)
        self.driver.close_app()

if __name__ == '__main__':
    unittest.main()
