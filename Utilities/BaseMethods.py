import time
import pyautogui as ui
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pynput.keyboard import Controller, Key

class BaseMethod:
    """The BasePage class holds all common functionality across the website.
    Also provides a nice wrapper when dealing with selenium functions that may
    not be easy to understand.
    """
    def __init__(self, driver):
        """ This function is called every time a new object of the base class is created"""
        self.driver = driver
    
    def click(self, by_locator):
        """ Performs click on web element whose locator is passed to it"""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def clickOnListItembyClassName(self, val, i):
        """ Performs click on web element whose locator is passed to it"""
        self.driver.find_elements(by=By.CLASS_NAME, value=val).__getitem__(i).click()

    def clickOnListItembyXpath(self, val, i):
        """ Performs click on web element whose locator is passed to it"""
        self.driver.find_elements(by=By.XPATH, value=val).__getitem__(i).click()

    def clickOnListItembyCSS(self, val, i):
        """ Performs click on web element whose locator is passed to it"""
        self.driver.find_elements(by=By.CSS_SELECTOR, value=val).__getitem__(i).click()

    def dropItembyClassName(self, val, i, x, y):
        droppable = self.driver.find_elements(by=By.CLASS_NAME, value=val).__getitem__(i)
        a = ActionChains(self.driver)
        a.move_to_element_with_offset(droppable,  x, y).perform()

    def dragItembyClassName(self, val, i,  x, y):
        """ Performs dragging on web element whose locator is passed to it """
        draggable = self.driver.find_elements(by=By.CLASS_NAME, value=val).__getitem__(i)
        a = ActionChains(self.driver)
        a.drag_and_drop_by_offset(draggable, x, y).perform()

    def dragItembyCSS(self, val, i,  x, y):
        """ Performs dragging on web element whose locator is passed to it"""
        draggable = self.driver.find_elements(by=By.CSS_SELECTOR, value=val).__getitem__(i)
        a = ActionChains(self.driver)
        a.drag_and_drop_by_offset(draggable, x, y).perform()

    def hover_on_element(self, by_locator):
        """ Performs hover on web element whose locator is passed to it"""
        a = ActionChains(self.driver)
        a.move_to_element(by_locator).perform()

    def send_text(self, by_locator, text):
        """ Performs text entry of the passed in text, in a web element whose locator is passed to it"""
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_title(self, title) -> str:
        """Returns the title of the page"""
        WebDriverWait(self.driver, 20).until(EC.title_is(title))
        return self.driver.title

    def get_element_text(self,by_locator):
        """ Performs get text operation on web element whose locator is passed to it"""
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_enabled(self, by_locator):
        """ check if an element is enables whose locator is passed to it"""
        element=WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator))
        return bool(element)
    
    def uploadItems_FromMyComputer(self, path):
        """ uploads files from my computer and """
        keyboard = Controller()
        keyboard.type(path)
        time.sleep(10)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        
    def clickOnScreen(self, horizontal, vertical):        
        ui.click(horizontal, vertical)

