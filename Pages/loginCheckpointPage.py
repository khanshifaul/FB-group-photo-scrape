from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Resources.Locators import Locators


class CheckpointPage:
    def __init__(self, driver):
        self.driver = driver
        self.aprovalcode = Locators.APPROVAL_CODE_TEXTBOX_ID
        self.continuebtn = Locators.CHECKPOINT_SUBMIT_BTN_ID
    
    def enter_aprovalcode(self, CODE):
        self.driver.find_element(By.ID, self.aprovalcode).clear()
        self.driver.find_element(By.ID, self.aprovalcode).send_keys(CODE)
    
    def press_continue(self):
        self.driver.find_element(By.ID, self.continuebtn).click()