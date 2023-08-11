from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PageObjects.BasePage import basepage
from PageObjects.SearchResult import searchResult

class MMTHome(basepage):
    FROM_CITY = "//label[@for='fromCity']"
    FROM_SEARCH = "//input[@placeholder='From']"
    SELECT_CITY = "// p[contains(text(), '<VALUE>')]"
    TO_CITY = "//label[@for='toCity']"
    TO_SEARCH = "//input[@placeholder='To']"

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def selectFromCity(self, fromSearch, fromcity):
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.FROM_CITY)))
        self.driver.find_element(By.XPATH, self.FROM_CITY).click()
        self.driver.find_element(By.XPATH, self.FROM_SEARCH).send_keys(fromSearch)
        city = self.SELECT_CITY.replace("<VALUE>", fromcity)
        self.wait.until(EC.presence_of_element_located((By.XPATH, city)))
        self.driver.find_element(By.XPATH, city).click()

    def selectToCity(self, toSearch, tocity):
        self.driver.find_element(By.XPATH, self.TO_CITY).click()
        self.driver.find_element(By.XPATH, self.TO_SEARCH).send_keys(toSearch)
        city = self.SELECT_CITY.replace("<VALUE>", tocity)
        self.wait.until(EC.presence_of_element_located((By.XPATH, city)))
        self.driver.find_element(By.XPATH, city).click()

    def enterDate(self,date):
        self.driver.find_element(By.XPATH, "//div[contains(@aria-label,'" + date + "')]").click()

    def clickSearch(self):
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Search']").click()
        flightResults = searchResult(self.driver)
        return flightResults


    def errorMsg(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='redText errorMsgText']")))
        isDisplayed = self.driver.find_element(By.XPATH, "//span[@class='redText errorMsgText']").is_displayed()
        assert isDisplayed == True
        errMsg = self.driver.find_element(By.XPATH, "//span[@class='redText errorMsgText']").text
        print(errMsg)
        assert errMsg == "From & To airports cannot be the same"


