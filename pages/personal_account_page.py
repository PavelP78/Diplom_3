from locators.locators import StellarBurgersLocators as Locators
from pages.base_page import StellarBurgerBasePage
from data import StellarBurgersLogin as Login
import allure
from selenium.webdriver.support.wait import WebDriverWait


class StellarBurgersPersonalAccountPage(StellarBurgerBasePage):
    def __init__(self, driver):
       # super().__init__(driver)
        self.driver = driver

    @allure.step(f"Клик по кнопке Личный кабинет")
    def click_main_enter_button(self):
        self.click_to_element(Locators.MAIN_ENTER_BUTTON)

    @allure.step(f"Заполнение формы email: {Login.MY_LOGIN}")
    def send_keys_to_placeholder_email(self):
        placeholder_name = self.driver.find_element(*Locators.EMAIL_FIELD)
        placeholder_name.send_keys(*Login.MY_LOGIN)

    @allure.step(f"Заполнение формы Пароль: {Login.MY_PASSWORD}")
    def send_keys_to_placeholder_password(self):
        placeholder_password = self.driver.find_element(*Locators.PASSWORD_FIELD)
        placeholder_password.send_keys(*Login.MY_PASSWORD)

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

