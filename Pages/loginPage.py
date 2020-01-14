from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Resources.Locators import Locators, Login_Data


class LoginPage:
    @classmethod
    def __init__(self, driver):
        self.driver = driver
        self.url = Login_Data.LOGIN_URL
        self.email = Locators.EMAIL_TEXTBOX_ID
        self.password = Locators.PASSWORD_TEXTBOX_ID
        self.login = Locators.LOGIN_BTN_ID
    
    def load(self):
        self.driver.get(self.url)

    def enter_email(self, EMAIL):
        self.driver.find_element(By.ID, self.email).clear()
        self.driver.find_element(By.ID, self.email).send_keys(EMAIL)

    def enter_password(self, PASSWORD):
        self.driver.find_element(By.ID, self.password).clear()
        self.driver.find_element(By.ID, self.password).send_keys(PASSWORD)

    def press_login(self):
        self.driver.find_element(By.ID, self.press_login).click()

    def show_error(self):
        if "facebook.com/login/" in self.driver.current_url:
            print('\nIncorrect Username or Password\n', 'red')
        else:
            pass

class CheckpointPage:
    @classmethod
    def __init__(self, driver):
        self.driver = driver
        self.aprovalcode = Locators.APPROVAL_CODE_TEXTBOX_ID
        self.continue = Locators.CHECKPOINT_SUBMIT_BTN_ID
    
    def enter_aprovalcode(self, CODE):
        self.driver.find_element(By.ID, self.aprovalcode).clear()
        self.driver.find_element(By.ID, self.aprovalcode).send_keys(CODE)
    
    def press_continue(self):
        self.driver.find_element(By.ID, self.continue).click()