from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class searchResult():
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def search_results(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='listingCard appendBottom5']")))
        allFlightDetails = self.driver.find_elements(By.XPATH, "//div[@class='listingCard appendBottom5']")
        totalFlights = len(allFlightDetails)
        print(totalFlights)
        return totalFlights

    def errMessage(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//p[@class='error-subtitle']")))
        msg = self.driver.find_element(By.XPATH, "//p[@class='error-subtitle']").text
        print(msg)
        assert msg == "We could not find flights for this search. Please go back to make a different selection."