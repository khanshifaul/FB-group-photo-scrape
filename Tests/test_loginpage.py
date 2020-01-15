import os, pickle, unittest, time
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import Options
from selenium.webdriver.firefox.webdriver import Service
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from selenium.webdriver.firefox.webdriver import DesiredCapabilities
from selenium.common.exceptions import *

from Pages.loginPage import LoginPage
from Pages.loginCheckpointPage import CheckpointPage
from Pages.groupHomePage import HomePage
from Pages.groupPhotoPage import PhotoPage


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
        firefox_capabilities = DesiredCapabilities.FIREFOX
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
        if self.driver.title == "Log in to Facebook | Facebook":
            login.enter_email("khanshifaul@gmail.com")
            login.enter_password("comexblue760")
            login.press_login()
            login.show_error()
        else:
            pass

    def test_LoginCheckPoint(self):
        checkpoint = CheckpointPage(self.driver)
        if "https://web.facebook.com/checkpoint/" in self.driver.current_url:
            checkpoint.enter_aprovalcode("21810277")
            checkpoint.press_continue()
        time.sleep(10)
        if (
            "https://web.facebook.com/checkpoint/" in self.driver.current_url
            and self.driver.find_element(By.TAG_NAME, "strong").get_text()
            == "Remember Browser"
        ):
            checkpoint.press_continue()

    def test_xGroupHomePage(self):
        homepage = HomePage(self.driver)
        time.sleep(30)
        homepage.search()

    def test_xGroupPhotoPage(self):
        photopage = PhotoPage(self.driver)
        photopage.load()
        photopage.openfPhoto()
        # for photopage.img():
        photopage.srcImg()
        photopage.nphoto()

    @classmethod
    def tearDownClass(cls):
        pickle.dump(cls.driver.get_cookies(), open("Cookies/cookies.pkl", "wb"))
        # cls.driver.close()
        # cls.driver.quit()
        print("Test Completed")


if __name__ == "__main__":
    unittest.main()
