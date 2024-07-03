from locators.locators import StellarBurgersLocators as Locators
import allure
from pages.base_page import StellarBurgerBasePage


class StellarBurgersLoginPage(StellarBurgerBasePage):

    @allure.step(f"Клик по кнопке Личный кабинет")
    def click_main_enter_button(self):
        self.click_to_element(Locators.MAIN_ENTER_BUTTON)

    @allure.step(f"Заполнение формы email")
    def send_keys_to_placeholder_email(self, api):
        placeholder_name = self.driver.find_element(*Locators.EMAIL_FIELD)
        placeholder_name.send_keys(api.get_login())

    @allure.step(f"Заполнение формы Пароль")
    def send_keys_to_placeholder_password(self, api):
        placeholder_password = self.driver.find_element(*Locators.PASSWORD_FIELD)
        placeholder_password.send_keys(api.get_password())

    @allure.step(f"Клик по кнопке Войти")
    def click_enter_button(self):
        self.click_to_element(Locators.ENTER_BUTTON)
