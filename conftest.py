import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from data import StellarBurgersUrl as Url


def get_driver(name):
    if name == "chrome":
        from selenium.webdriver.chrome.service import Service as ChromeService
        service = ChromeService(executable_path=ChromeDriverManager().install())
        return webdriver.Chrome(service=service)
    elif name == "firefox":
        from selenium.webdriver.firefox.service import Service as FirefoxService
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        return webdriver.Firefox(service=service)
    else:
        raise TypeError("Driver is not found")


@pytest.fixture(params=["firefox"])
def driver(request):
    driver = get_driver(request.param)
    driver.get(Url.URL_MAIN)
    driver.maximize_window()
    driver.delete_all_cookies()
    yield driver
    driver.quit()
