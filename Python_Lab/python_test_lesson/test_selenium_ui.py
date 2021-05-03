"""
#############################################################################
Selenium:IntegrationテストでのWebUIテストを自動化する
参考：https://selenium-python.readthedocs.io/

#############################################################################

"""

import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class PythonOrgTest(unittest.TestCase):
    def setUp(self):
        # FireFoxを開く
        self.driver = webdriver.Firefox()
        
    def tearDown(self):
        self.driver.close()
        
    def test_python_org(self):
        # URLにアクセスする
        self.driver.get('http://python.org')
        # time.sleep(5)
        
        # titleタグに'Python'が含まれているかテストする
        self.assertIn('Python', self.driver.title)
        # time.sleep(5)
        
        self.driver.find_element_by_link_text('Downloads').click()
        
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, 'widget-title')
            )
        )
        
        # classに'widget-title'であるテキストに'Looking~'が含まれているかテストする
        self.assertEqual('Looking for a specific release?', element[1].text)
        
        # 検索ボックスにpyconと打って、検索結果が出てくることをテスト
        element = self.driver.find_element_by_name('q')
        element.clear()
        element.send_keys('pycon')
        element.send_keys(Keys.RETURN)
        time.sleep(5)
        assert 'No results found' not in self.driver.page_source

if __name__ == '__main__':
    unittest.main()