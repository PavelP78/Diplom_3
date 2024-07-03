from data import StellarBurgersUrl as Url
import allure
from pages.personal_account_page import StellarBurgersPersonalAccountPage


class TestStellarBurgersPersonalAccount:

    @allure.title('Проверка: переход по клику на «Личный кабинет»')
    def test_personal_account_button_click(self, driver, pages):
        pages.click_main_enter_button()
        assert driver.current_url == f'{Url.URL_LOGIN}', "Url is wrong"

    @allure.title('Проверка: переход в раздел «История заказов»')
    def test_order_history_button_click(self, enter_and_delete_user, driver):
        pages = StellarBurgersPersonalAccountPage(driver)
        pages.click_authorized_user_personal_account_button()
        pages.click_order_history_button()
        assert driver.current_url == f'{Url.URL_ORDER_HISTORY}', "Url is wrong"

    @allure.title('Проверка: выход из аккаунта')
    def test_exit_button_click(self, enter_and_delete_user, driver):
        pages = StellarBurgersPersonalAccountPage(driver)
        pages.click_authorized_user_personal_account_button()
        pages.click_exit_button()
        assert driver.current_url == f'{Url.URL_ACCOUNT_PROFILE}', "Url is wrong"
