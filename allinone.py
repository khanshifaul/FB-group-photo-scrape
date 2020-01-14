import os, unittest, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import Options
from selenium.webdriver.firefox.webdriver import Service
from selenium.webdriver.firefox.webdriver import FirefoxBinary
from selenium.webdriver.firefox.webdriver import DesiredCapabilities


driver_path = str(os.path.abspath("../../../../mnt/c/") + "/geckodriver.exe")
# driver_path = "driver/geckodriver"
firefox_service = Service(driver_path)
firefox_options = Options()
firefox_options.headless = False
firefox_capabilities = DesiredCapabilities.FIREFOX
firefox_capabilities["marionette"] = False
driver = webdriver.Firefox(
    service=firefox_service,
    options=firefox_options,
    desired_capabilities=firefox_capabilities,
)
driver.implicitly_wait(15)
driver.set_page_load_timeout(30)
driver.set_script_timeout(30)
driver.set_window_rect(x=0, y=920, width=775, height=420)

# time.sleep(10)
driver.get("http://facebook.com")
time.sleep(20)
if driver.title == "Facebook – log in or sign up":
    driver.find_element(By.ID, "email").send_keys("khanshifaul@gmail.com")
    driver.find_element(By.ID, "pass").send_keys("comexblue760")
    driver.find_element(By.ID, "loginbutton").click()
    driver.save_screenshot("screenshot/shot1.png")
    if "https://web.facebook.com/checkpoint/" in driver.current_url:
        driver.find_element(By.ID, "approvals_code").send_keys("70967135")
        driver.find_element(By.ID, "checkpointSubmitButton").click()
        driver.save_screenshot("screenshot/shot2.png")
        if (
            "https://web.facebook.com/checkpoint/" in driver.current_url
            and driver.find_element(By.ID, "approvals_code")
        ):
            print("Incorrect approvals code")
            driver.find_element(By.ID, "approvals_code").send_keys("69482435")
            driver.find_element(By.ID, "checkpointSubmitButton").click()
        elif (
            "https://web.facebook.com/checkpoint/" in driver.current_url
            and driver.find_element(By.TAG_NAME, "strong").get_text()
            == "Remember Browser"
        ):
            driver.find_element(By.ID, "checkpointSubmitButton").click()
        else:
            print("error")
    elif driver.titile == "Log in to Facebook | Facebook":
        print("Incorrect Username or Password")
    else:
        pass
else:
    driver.close()
    driver.get("https://web.facebook.com/groups/BOBO.BD/"+"photos")
    driver.find_element(By.)

driver.save_screenshot("screenshot/shot.png")
# driver.quit()
# "Sorry, this content isn't available right now"