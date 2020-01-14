import unittest, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import Options
from selenium.webdriver.firefox.webdriver import Service
from selenium.webdriver.firefox.webdriver import FirefoxBinary
from selenium.webdriver.firefox.webdriver import DesiredCapabilities
from progress.bar import FillingSquaresBar


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        driver_path = str(os.path.abspath("../../../../mnt/c/") + "/geckodriver.exe")
        # driver_path = "driver/geckodriver"
        firefox_service = Service(driver_path)
        firefox_options = Options()
        firefox_options.headless = False
        firefox_capabilities = DesiredCapabilities.FIREFOX.copy()
        firefox_capabilities["marionette"] = True
        cls.driver = webdriver.Firefox(
            service=firefox_service,
            options=firefox_options,
            desired_capabilities=firefox_capabilities
        )
        cls.driver.implicitly_wait(10)
        cls.driver.set_page_load_timeout(30)
        cls.driver.set_script_timeout(30)
        cls.driver.set_window_rect(x=0, y=920, width=775, height=420)

    def test_login(self):
        self.driver.get("http://facebook.com")
        self.driver.find_element(By.ID, "email").send_keys("khanshifaul@gmail.com")
        self.driver.find_element(By.ID, "pass").send_keys("comexblue760")
        self.driver.find_element(By.ID, "loginbutton").click()
        self.driver.save_screenshot("screenshot/shot1.png")

    def test_auth(self):
        self.driver.find_element(By.ID, "approvals_code").send_keys("88481003")
        self.driver.find_element(By.ID, "checkpointSubmitButton").click()
        self.driver.save_screenshot("screenshot/shot2.png")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__ == "__main__":
    unittest.main()