import pytest
from selenium import webdriver
from configparser import ConfigParser
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def pytest_addoption(parser):
    parser.addoption(
        "--browser-name",
        action="store",
        default="chrome",
        help="Browser: chrome or firefox or edge"
    )

@pytest.fixture(scope="function")
def driver(request):
    # Read URL from config.ini
    config = ConfigParser()
    config.read('config.ini')
    link = config['GuviURL']['url']

    browser_name = request.config.getoption("--browser-name")

    if browser_name == 'firefox':
        _driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser_name == 'chrome':
        _driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser_name == 'edge':
        _driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    _driver.maximize_window()
    _driver.get(link)   # Open the URL once here

    yield _driver

    _driver.quit()
