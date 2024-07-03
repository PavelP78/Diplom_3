from locators.locators import StellarBurgersLocators as Locators
from pages.base_page import StellarBurgerBasePage
import allure


class StellarBurgersOrderFeedPage(StellarBurgerBasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    @allure.step('Добавить ингридиент в заказ')
    def add_filling_to_order(self):
        self.drag_and_drop_element(Locators.ROLLS_PICTURE, Locators.ORDER_BASKET_UP)

    @allure.step(f"Клик по кнопке Войти")
    def click_enter_button(self):
        self.click_to_element(Locators.ENTER_BUTTON)

    @allure.step(f"Клик по кнопке Оформить заказ")
    def click_order_button(self):
        self.click_to_element(Locators.ORDER_BUTTON)

    @allure.step("Получение текста Ваш заказ начали готовить")
    def get_order_text(self):
        order_text = self.get_text(Locators.ORDER_TEXT)
        return order_text

    @allure.step(f"Клик по кнопке История заказов")
    def click_order_history_button(self):
        self.click_to_element(Locators.ORDER_HISTORY_BUTTON)

    @allure.step(f"значение Номер заказа(последний в списке) пользователя в разделе История заказов")
    def get_order_user_number_first_in_order_history(self):
        return self.get_actually_text(Locators.ORDER_USER_NUMBER_LAST_IN_ORDER_HISTORY)

    @allure.step(f"Клик по кнопке Лента заказов")
    def click_order_feed_button(self):
        self.click_to_element(Locators.ORDER_FEED_BUTTON)

    @allure.step(f"Закрытие всплывающего окна созданного заказа")
    def click_close_pop_up_order_button(self):
        self.click_to_element(Locators.CLOSE_POP_UP_ORDER_BUTTON)

    @allure.step(f"значение Номер заказа(первый в списке) пользователя в разделе Лента заказов")
    def get_order_user_number_first_in_feed(self):
        return self.get_actually_text(Locators.ORDER_USER_NUMBER_FIRST_IN_FEED)

    @allure.step(f"Клик по кнопке Личный кабинет авторизированного пользователя")
    def click_authorized_user_personal_account_button(self):
        self.click_to_element(Locators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step(f"значение счетчика выполненных заказов за все время в разделе Лента заказов")
    def get_value_order_meter_all_time(self):
        return self.get_actually_text(Locators.ORDER_METER_ALL_TIME)

    @allure.step(f"значение счетчика выполненных заказов за сегодня в разделе Лента заказов")
    def get_value_order_meter_today(self):
        return self.get_actually_text(Locators.ORDER_METER_TODAY)

    @allure.step(f"Клик по кнопке Конструктор")
    def click_design_button(self):
        self.click_to_element(Locators.DESIGNER_BUTTON)

    @allure.step(f"значение счетчика заказа в разделе В работе")
    def get_value_order_meter_in_progress_field(self):
        return self.get_actually_text(Locators.ORDER_IN_PROGRESS)
