import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(params=["chrome"], scope="class")
def web_driver(request):
        
    if request.param == "chrome":
        w_driver = webdriver.Chrome(ChromeDriverManager().install())
    else:
        w_driver = webdriver.Edge()
        
    request.cls.driver = w_driver
    w_driver.get("http://www.google.com")
    # wait for 10 seconds implicitly
    w_driver.implicitly_wait(10)
    #maximize the window
    w_driver.maximize_window()
    yield
    # Close browser
    w_driver.close()