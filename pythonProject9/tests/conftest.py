

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(params=["chrome","firefox"])
def driver(request):
    # browser=request.config.getoption("--browser")
    browser=request.param
    print(f"creating {browser} driver")
    if browser=="chrome":
        mydriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser=="firefox":
        mydriver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise TypeError(f"Expected 'chrome' or 'firefox' but got {browser}")

    yield mydriver
    # any text after the yield will be retured after the test is over
    print(f"closing {browser} driver")
    mydriver.quit()

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser to execute the tests (chrome or firefox)"
    )