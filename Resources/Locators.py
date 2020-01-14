from selenium.webdriver.common.by import By

class Locators():
    # --- Login Page Locators ---
    EMAIL_TEXTBOX_ID = "email"
    PASSWORD_TEXTBOX_ID = "pass"
    LOGIN_BTN_ID = "loginbutton"

    # --- Login Checkpoint (AprovalCode) Page Locators ---
    APPROVAL_CODE_TEXTBOX_ID = "approvals_code"
    CHECKPOINT_SUBMIT_BTN_ID = "checkpointSubmitButton"

    # --- Login Checkpoint (SaveBrowser) Page Locators ---

    # --- Goup Page Locators ---
    FIRST_PHOTO_XPATH = "//tr[1]//td[1]//div[1]"
    NEXT_PHOTO_XPATH = "//a[@class='snowliftPager next hilightPager']"
    IMG_XPATH = "//img[@class='spotlight']"
    IMG_SRC = ""
    DL_BTN_XPATH = ""

class Login_Data:
    LOGIN_URL = "http://facebook.com/login"