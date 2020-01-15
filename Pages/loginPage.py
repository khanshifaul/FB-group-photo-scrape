import pickle
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Resources.Locators import Locators, Data


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = Data.LOGIN_URL
        self.email = Locators.EMAIL_TEXTBOX_ID
        self.password = Locators.PASSWORD_TEXTBOX_ID
        self.login = Locators.LOGIN_BTN_ID
    
    def load(self):
        self.driver.get(self.url)
        cookies = pickle.load(open("Cookies/cookies.pkl", "rb"))
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()

    def enter_email(self, EMAIL):
        self.driver.find_element(By.ID, self.email).clear()
        self.driver.find_element(By.ID, self.email).send_keys(EMAIL)

    def enter_password(self, PASSWORD):
        self.driver.find_element(By.ID, self.password).clear()
        self.driver.find_element(By.ID, self.password).send_keys(PASSWORD)

    def press_login(self):
        self.driver.find_element(By.ID, self.login).click()

    def show_error(self):
        if "facebook.com/login/" in self.driver.current_url:
            print('\nIncorrect Username or Password\n', 'red')
        else:
            pass
