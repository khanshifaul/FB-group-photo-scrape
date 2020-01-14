import os, pickle, unittest
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import Options
from selenium.webdriver.firefox.webdriver import Service
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from selenium.webdriver.firefox.webdriver import DesiredCapabilities
from selenium.common.exceptions import *

from Pages.loginPage import LoginPage


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        driver_path = str(
            os.path.abspath("../../../../../mnt/c/") + "/geckodriver.exe"
        )  # For WSL Linux
        # driver_path = "driver/geckodriver.exe"  # For Windows
        # driver_path = "driver/geckodriver"  # For Linux
        firefox_service = Service(driver_path)
        firefox_options = Options()
        firefox_options.headless = False
        firefox_profile = FirefoxProfile()
        firefox_profile.set_preference(
            "browser.download.manager.showWhenStarting", False
        )
        firefox_profile.set_preference("browser.download.dir", "/Images")
        firefox_capabilities = DesiredCapabilities.FIREFOX.copy()
        firefox_capabilities["marionette"] = False
        cls.driver = webdriver.Firefox(
            service=firefox_service,
            options=firefox_options,
            desired_capabilities=firefox_capabilities,
            firefox_profile=firefox_profile,
        )
        cls.driver.implicitly_wait(10)
        cls.driver.set_page_load_timeout(30)
        cls.driver.set_script_timeout(30)
        cls.driver.set_window_rect(x=0, y=920, width=775, height=420)

    def test_Login(self):
        login = LoginPage(self.driver)
        login.load()
        if driver.title == "Log in to Facebook | Facebook":
            login.enter_email("01719789248")
            login.enter_password("01719789248")
            login.press_login()
            login.show_error()
        else:
            pass

    def test_LoginCheckPoint(self):
        if "https://web.facebook.com/checkpoint/" in driver.current_url:
            driver.find_element(By.ID, "approvals_code").send_keys("70967135")
            driver.find_element(By.ID, "checkpointSubmitButton").click()


    @classmethod
    def tearDownClass(cls):
        pickle.dump(driver.get_cookies(), open(".Cookies/cookies.pkl", "wb"))
        # cls.driver.close()
        # cls.driver.quit()
        print("Test Completed")


if __name__ == "__main__":
    unittest.main()
