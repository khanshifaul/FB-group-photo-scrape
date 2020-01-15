import pickle
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Resources.Locators import Locators, Data


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.search = Data.SEARCH_TEXTBOX_XPATH
        self.searchkey = Data.SEARCH_KEY
        self.group = Data.GROUP_XPATH

    def search(self):
        self.driver.find_element(By.XPATH, self.search).send_keys(self.searchkey).send_keys(Keys.RETURN)
        self.driver.find_element(By.XPATH, self.group).click()

    def checkJoined(self):
        self.driver.find_element(By.ID, "").click()
