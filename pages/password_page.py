from locators.locators import StellarBurgersLocators as Locators
from pages.base_page import StellarBurgerBasePage
from data import StellarBurgersLogin as Login
import allure


class StellarBurgersPasswordPage(StellarBurgerBasePage):

    def __init__(self, driver):
       # super().__init__(driver)
        self.driver = driver

    @allure.step(f"Клик по кнопке Личный кабинет")
    def click_main_enter_button(self):
        self.click_to_element(Locators.MAIN_ENTER_BUTTON)

    @allure.step(f"Клик по кнопке Восстановить пароль")
    def click_recovery_password_button(self):
        self.click_to_element(Locators.BUTTON_PASSWORD_RECOVERY_FORM)

    @allure.step(f"Заполнение формы email: {Login.MY_LOGIN}")
    def send_keys_to_placeholder_email(self):
        placeholder_name = self.driver.find_element(*Locators.EMAIL_FIELD_RECOVERY_PASSWORD)
        placeholder_name.send_keys(*Login.MY_LOGIN)

    @allure.step(f"Клик по кнопке Восстановить")
    def click_recovery_button(self):
        self.click_to_element(Locators.ENTER_BUTTON_PASSWORD_RECOVERY_FORM)

    @allure.step(f"Клик по кнопке показать пароль")
    def click_show_password_button(self):
        self.click_to_element(Locators.SHOW_PASSWORD_BUTTON)

    @allure.step(f"видимость поля Пароль")
    def placeholder_email_is_active(self):
        return self.element_is_visible(Locators.ACTIVE_PASSWORD_FIELD)
