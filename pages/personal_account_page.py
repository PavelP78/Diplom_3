from locators.locators import StellarBurgersLocators as Locators
from pages.base_page import StellarBurgerBasePage
import allure


class StellarBurgersPersonalAccountPage(StellarBurgerBasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

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

    @allure.step(f"Клик по кнопке Личный кабинет авторизированного пользователя")
    def click_authorized_user_personal_account_button(self):
        self.click_to_element(Locators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step(f"Клик по кнопке История Заказов")
    def click_order_history_button(self):
        self.click_to_element(Locators.ORDER_HISTORY_BUTTON)

    @allure.step(f"Клик по кнопке Выход")
    def click_exit_button(self):
        self.click_to_element(Locators.EXIT_BUTTON)
