import pickle
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Resources.Locators import Locators, Data


class PhotoPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = Data.GROUP_URL + "photos/"
        self.fphoto = Data.FIRST_PHOTO_XPATH
        self.img = Data.IMG_XPATH
        self.imgsrc = Data.IMG_SRC
        self.nphoto = Data.NEXT_PHOTO_XPATH

    def load(self):
        self.driver.find_element(By.XPATH, "//div[@id='u_jsonp_6_4']//div[7]//a[1]").click()

    def openPhotoF(self):
        self.driver.find_element(By.XPATH, self.fphoto).click()
    
    def Img(self):
        self.driver.find_element(By.XPATH, self.img)

    def srcImg(self):
        imgsrc = self.driver.find_element(By.XPATH, self.img).getattr("src")
        print(imgsrc)
    
    def openPhotoN(self):
        self.driver.find_element(By.XPATH, self.nphoto).click()
