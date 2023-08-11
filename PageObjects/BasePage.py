import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
class basepage():
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def closeFrame(self):
        try:
            self.wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@id='webklipper-publisher-widget-container-notification-frame']")))
            #iframe = self.driver.find_element(By.XPATH, "//iframe[@id='webklipper-publisher-widget-container-notification-frame']")
            self.driver.find_element(By.XPATH, "//i[@class='wewidgeticon we_close']").click()
            # driver.switch_to.frame(iframe)
        except:
            print("Frame is not displayed")

    def enterUser(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "username")))
        self.driver.find_element(By.ID, "username").send_keys("ppkonnur@gmail.com")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Continue']")))
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Continue']").click()

    def closeUserDailog(self):
        actionChain = ActionChains(self.driver)
        self.wait.until(EC.presence_of_element_located((By.ID, "username")))
        actionChain.move_by_offset(100,10).click().perform()
