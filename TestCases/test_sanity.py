from selenium import webdriver
from PageObjects.MMTHome import MMTHome
import unittest
import pytest
from ddt import ddt, data, unpack,file_data
from Utilities.Utils import utils

@pytest.mark.usefixtures("setup")
@ddt
class Test_MMTSanity(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.home = MMTHome(self.driver)

    @data(("MakeMyTrip",""))
    @unpack
    def test_MMT_001(self,MMTTitle, x):
        title = self.driver.title
        print(title)
        assert title == "MakeMyTrip - #1 Travel Website 50% OFF on Hotels, Flights & Holiday"

    @data(("Pun","Pune","Bang","Bangkok","Aug 26 2023"),("New","New Delhi","Bang","Bangkok","Aug 20 2023"))
    @unpack
    # @data(*utils.readDataFromExcel("D:\\PythonTraining\\AutomationFramework\\TestData\\TestData.xlsx","Sheet1"))
    # @unpack
    def test_MMT_002(self, fromSearch, fromcity,toSearch,tocity,date):
        # fromSearch = "Pun"
        # fromcity = "Pune"
        # toSearch = "Bang"
        # tocity = "Bangkok"
        # date = "Aug 26 2023"

        #Close Iframe
        # self.home = MMTHome(self.driver)
        self.home.closeFrame()

        #Enter User
        #self.home.enterUser()
        self.home.closeUserDailog()

        #selecting from city
        self.home.selectFromCity(fromSearch,fromcity)

        #Select Tocity
        self.home.selectToCity(toSearch, tocity)

        #Select Date
        self.home.enterDate(date)

        #Click search
        result = self.home.clickSearch()
        totalFlights = result.search_results()
        assert totalFlights > 0

    @pytest.mark.skip
    def test_MMT_003(self):
        fromSearch = "Pun"
        fromcity = "Pune"
        toSearch = "Pun"
        tocity = "Pune"
        date = "Aug 26 2023"

        #Close Iframe
        self.home.closeFrame()

        #Enter User
        #self.home.enterUser()
        self.home.closeUserDailog()

        #selecting from city
        self.home.selectFromCity(fromSearch, fromcity)

        #Select Tocity
        self.home.selectToCity(toSearch, tocity)

        self.home.errorMsg()

    @pytest.mark.skip
    def test_MMT_004(self):
        fromSearch = "Hub"
        fromcity = "Hubli"
        toSearch = "Pal"
        tocity = "Palermo, Italy"
        date = "Aug 26 2023"

        #Close Iframe
        self.home.closeFrame()

        #Enter User
        #self.home.enterUser()
        self.home.closeUserDailog()

        #selecting from city
        self.home.selectFromCity(fromSearch, fromcity)

        #Select Tocity
        self.home.selectToCity(toSearch, tocity)

        # Select Date
        self.home.enterDate(date)

        # Click search
        result = self.home.clickSearch()
        result.errMessage()
