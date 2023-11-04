import time
import pytest
from PageObjects.googleHome import GoogleHome
from driver.baseclass import BaseClass
import sys
sys.path.append('C:\\Users\\HP\\PycharmProjects\\PracticeprojectBMQ\\project1\\driver')
from driver.conftest import web_driver
# from webdriver_manager.chrome import ChromeDriverManager

# @pytest.mark.usefixtures("web_driver")
class TestIt(BaseClass):
    def test_Google(self):
      self.searchProcess = GoogleHome(self.driver)
      self.searchProcess.sendValue()
      time.sleep(10)
        

# def test_Google_1():
#     driver = webdriver.Chrome(ChromeDriverManager().install())
#     driver.implicitly_wait(10)
#     driver.get('http://www.google.com')
#     assert driver.title == "Google"
#     driver.quit()
# def test_Google_2():
#     driver = webdriver.Chrome(ChromeDriverManager().install())
#     driver.implicitly_wait(10)
#     driver.get('http://www.google.com')
#     assert driver.title == "Google"
#     driver.quit()