from selenium.webdriver.common.by import By

class Locators:
    # --- Login Page Locators ---
    EMAIL_TEXTBOX_ID = "email"
    PASSWORD_TEXTBOX_ID = "pass"
    LOGIN_BTN_ID = "loginbutton"

    # --- Login Checkpoint (AprovalCode) Page Locators ---
    APPROVAL_CODE_TEXTBOX_ID = "approvals_code"
    CHECKPOINT_SUBMIT_BTN_ID = "checkpointSubmitButton"

    SEARCH_TEXTBOX_XPATH = "//div[@id='u_3_2']//input[@placeholder='Search']"

    # --- Goup Page Locators ---
    GROUP_XPATH = "//a[contains(text(),'/ Bogra Online Blood Do')]"
    JOIN_BTN_ID = "joinButton_131738940610053"
    FIRST_PHOTO_XPATH = "//tr[1]//td[1]//div[1]"
    NEXT_PHOTO_XPATH = "//a[@class='snowliftPager next hilightPager']"
    IMG_XPATH = "//img[@class='spotlight']"
    IMG_SRC = ""

class Data:
    LOGIN_URL = "http://facebook.com/login"
    SEARCH_KEY = "bogra online blood donation organisation"
