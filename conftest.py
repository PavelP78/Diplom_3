import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from data import StellarBurgersUrl as Url
from api_page import StellarBurgersAPI
from pages.login_page import StellarBurgersLoginPage
from pages.main_function_page import StellarBurgersMainFunctionPage


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


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    driver = get_driver(request.param)
    driver.get(Url.URL_MAIN)
    driver.maximize_window()
    driver.delete_all_cookies()
    yield driver
    driver.quit()


@pytest.fixture
def pages(driver):
    return StellarBurgersMainFunctionPage(driver)


@pytest.fixture
def enter_and_delete_user(driver):
    stellar_burgers_api = StellarBurgersAPI()
    sign_up_data = stellar_burgers_api.sign_up_data
    new_user_response = stellar_burgers_api.create_new_user(sign_up_data)
    access_token = stellar_burgers_api.get_access_token(new_user_response)
    assert new_user_response.status_code == 200, "Новый пользователь не создан"
    pages = StellarBurgersLoginPage(driver)
    pages.click_main_enter_button()
    pages.send_keys_to_placeholder_email(stellar_burgers_api)
    pages.send_keys_to_placeholder_password(stellar_burgers_api)
    pages.click_enter_button()
    yield
    response = stellar_burgers_api.delete_user(access_token)
    assert response.status_code == 202, "Пользователь не удален"
