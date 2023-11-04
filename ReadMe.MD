# PageObjectModel Framework - Demo

## `Package` Directory

- `Utilities/`: The main application entry point.

  - `__init__.py`: always blank
  - `Common.py or BaseMethods.py`: contains all the reused methods

- `Data/`: Directory containing the data.

  - `__init__.py`: always blank
  - `login_data.py`: contains all the input data and others data for login page.

  - `registration_data.py`: contains all the input data and others data for user registration.

- `PageObject/`: Directory containing the main application code.

  - `__init__.py`: always blank

  - `page_1.py`: Code for login.

  - `page_2.py`: Code for registration.

- `Test/`: Directory containing the main application code.

  - `__init__.py`: always blank
  - `conftest.py`: contains full driver setup under `@pytest.fixture` function. And in code the fixture funtion will always exectues before any other function.  
    `import pytest`
    `from selenium import webdriver`
    `from webdriver_manager.chrome import ChromeDriverManager`

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

  - `baseclass.py`: Use the fixture under an empty class and pass that class. So the this class can be reuse

    -`import pytest`

        @pytest.mark.usefixtures("web_driver")
        class BaseClass:
        pass

  - `test_login.py`: test file will inherit the `BaseClass` and It will instantiate all `Object` those are relevant in the `pageObject\` package

        class TestIt(BaseClass):
            def test_Login(self):
            self.login = LoginPage(self.driver)
            self.login.loginProcess()
            time.sleep(10)

  - `test_registration.py`: same as test_login.

- `Open CMD/`: Directory containing the main application code.

  - `pytest Test\test_login.py -v `: press enter and see the result
