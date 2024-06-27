from data import StellarBurgersUrl as Url
import allure
from pages.password_page import StellarBurgersPasswordPage


class TestStellarBurgersPasswordRecovery:

    @allure.title('Проверка: переход на страницу восстановления пароля по кнопке «Восстановить пароль')
    def test_recovery_password_button_click(self, driver):
        pages = StellarBurgersPasswordPage(driver)
        pages.click_main_enter_button()
        pages.click_recovery_password_button()
        assert driver.current_url == f'{Url.URL_FORGOT_PASSWORD}', "Url is wrong"

    @allure.title('Проверка: ввод почты и клик по кнопке «Восстановить»')
    def test_email_enter_and_recovery_button_click(self, driver):
        pages = StellarBurgersPasswordPage(driver)
        pages.click_main_enter_button()
        pages.click_recovery_password_button()
        pages.send_keys_to_placeholder_email()
        pages.click_recovery_button()
        assert driver.current_url == f'{Url.URL_LOGIN}', "Url is wrong"

    @allure.title('Проверка: клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_make_see_show_password_button_click(self, driver):
        pages = StellarBurgersPasswordPage(driver)
        pages.click_main_enter_button()
        pages.click_recovery_password_button()
        pages.send_keys_to_placeholder_email()
        pages.click_recovery_button()
        pages.click_show_password_button()
        assert pages.placeholder_email_is_active(), "placeholder not active"
