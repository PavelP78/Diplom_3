from data import StellarBurgersUrl as Url
import allure
from pages.password_page import StellarBurgersPasswordPage
from api_page import StellarBurgersAPI


class TestStellarBurgersPasswordRecovery:

    @allure.title('Проверка: переход на страницу восстановления пароля по кнопке «Восстановить пароль')
    def test_recovery_password_button_click(self, driver):
        pages = StellarBurgersPasswordPage(driver)
        pages.click_main_enter_button()
        pages.click_recovery_password_button()
        assert driver.current_url == f'{Url.URL_FORGOT_PASSWORD}', "Url is wrong"

    @allure.title('Проверка: ввод почты и клик по кнопке «Восстановить»')
    def test_email_enter_and_recovery_button_click(self, driver):
        stellar_burgers_api = StellarBurgersAPI()
        sign_up_data = stellar_burgers_api.sign_up_data
        new_user_response = stellar_burgers_api.create_new_user(sign_up_data)
        access_token = stellar_burgers_api.get_access_token(new_user_response)
        assert new_user_response.status_code == 200, "Новый пользователь не создан"
        pages = StellarBurgersPasswordPage(driver)
        pages.click_main_enter_button()
        pages.click_recovery_password_button()
        pages.send_keys_to_placeholder_email(stellar_burgers_api)
        pages.click_recovery_button()
        assert driver.current_url == f'{Url.URL_LOGIN}', "Url is wrong"
        response = stellar_burgers_api.delete_user(access_token)
        assert response.status_code == 202, "Пользователь не удален"

    @allure.title('Проверка: клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_make_see_show_password_button_click(self, driver):
        stellar_burgers_api = StellarBurgersAPI()
        sign_up_data = stellar_burgers_api.sign_up_data
        new_user_response = stellar_burgers_api.create_new_user(sign_up_data)
        access_token = stellar_burgers_api.get_access_token(new_user_response)
        assert new_user_response.status_code == 200, "Новый пользователь не создан"
        pages = StellarBurgersPasswordPage(driver)
        pages.click_main_enter_button()
        pages.click_recovery_password_button()
        pages.send_keys_to_placeholder_email(stellar_burgers_api)
        pages.click_recovery_button()
        pages.click_show_password_button()
        assert pages.placeholder_email_is_active(), "placeholder not active"
        response = stellar_burgers_api.delete_user(access_token)
        assert response.status_code == 202, "Пользователь не удален"
