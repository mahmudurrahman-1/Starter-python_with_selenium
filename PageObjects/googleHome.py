from selenium.webdriver.common.by import By
from Utilities.BaseMethods import BaseMethod 


searchField = (By.ID, "APjFqb")

class GoogleHome(BaseMethod):
    def __init__(self, driver):
        super().__init__(driver)
    
    def sendValue(self):
        self.send_text(searchField, "abc")
