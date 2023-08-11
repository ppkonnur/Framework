import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManagere
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from Utilities.Utils import utils
from configparser import ConfigParser

driver = None
@pytest.fixture(scope='function',autouse=True)
def setup(request):
    browser = getConfig("browser")
    URL = getConfig("URL")
    if browser == 'Chrome':
        driver = webdriver.Chrome(service=Service("D:\\PythonTraining\\AutomationFramework\\Drivers\\chromedriver.exe"))
        # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser == 'FireFox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        print("Invalid Browser")
        raise Exception("Invalid Browser")
    driver.get(URL)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    util = utils(driver)
    tcName = request.node.name
    util.takeScreenshot(tcName)
    driver.close()

def getConfig(configKey):
    config = ConfigParser()
    config.read("AppConfig.ini")
    return config['AppConfig'][configKey]

def pytest_html_report_title(report):
    type = getConfig("Type")
    version = getConfig("Version")
    report.title = "MakeMyTrip {} Report on Version {}".format(type,version)
    # report.title = "My very own title!"