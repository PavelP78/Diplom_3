from data import StellarBurgersUrl as Url
import allure
from pages.personal_account_page import StellarBurgersPersonalAccountPage
from api_page import StellarBurgersAPI


class TestStellarBurgersPersonalAccount:

    @allure.title('Проверка: переход по клику на «Личный кабинет»')
    def test_personal_account_button_click(self, driver):
        pages = StellarBurgersPersonalAccountPage(driver)
        pages.click_main_enter_button()
        assert driver.current_url == f'{Url.URL_LOGIN}', "Url is wrong"

    @allure.title('Проверка: переход в раздел «История заказов»')
    def test_order_history_button_click(self, driver):
        stellar_burgers_api = StellarBurgersAPI()
        sign_up_data = stellar_burgers_api.sign_up_data
        new_user_response = stellar_burgers_api.create_new_user(sign_up_data)
        access_token = stellar_burgers_api.get_access_token(new_user_response)
        assert new_user_response.status_code == 200, "Новый пользователь не создан"
        pages = StellarBurgersPersonalAccountPage(driver)
        pages.click_main_enter_button()
        pages.send_keys_to_placeholder_email(stellar_burgers_api)
        pages.send_keys_to_placeholder_password(stellar_burgers_api)
        pages.click_enter_button()
        pages.click_authorized_user_personal_account_button()
        pages.click_order_history_button()
        assert driver.current_url == f'{Url.URL_ORDER_HISTORY}', "Url is wrong"
        response = stellar_burgers_api.delete_user(access_token)
        assert response.status_code == 202, "Пользователь не удален"

    @allure.title('Проверка: выход из аккаунта')
    def test_exit_button_click(self, driver):
        stellar_burgers_api = StellarBurgersAPI()
        sign_up_data = stellar_burgers_api.sign_up_data
        new_user_response = stellar_burgers_api.create_new_user(sign_up_data)
        access_token = stellar_burgers_api.get_access_token(new_user_response)
        assert new_user_response.status_code == 200, "Новый пользователь не создан"
        pages = StellarBurgersPersonalAccountPage(driver)
        pages.click_main_enter_button()
        pages.send_keys_to_placeholder_email(stellar_burgers_api)
        pages.send_keys_to_placeholder_password(stellar_burgers_api)
        pages.click_enter_button()
        pages.click_authorized_user_personal_account_button()
        pages.click_exit_button()
        assert driver.current_url == f'{Url.URL_ACCOUNT_PROFILE}', "Url is wrong"
        response = stellar_burgers_api.delete_user(access_token)
        assert response.status_code == 202, "Пользователь не удален"
