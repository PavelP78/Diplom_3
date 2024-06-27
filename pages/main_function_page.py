from locators.locators import StellarBurgersLocators as Locators
from pages.base_page import StellarBurgerBasePage
from data import StellarBurgersLogin as Login
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class StellarBurgersMainFunctionPage(StellarBurgerBasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step(f"Клик по кнопке Лента Заказов")
    def click_order_feed_button(self):
        self.click_to_element(Locators.ORDER_FEED_BUTTON)

    @allure.step(f"Клик по кнопке Конструктор")
    def click_design_button(self):
        self.click_to_element(Locators.DESIGNER_BUTTON)

    @allure.step(f"Клик по кнопке Личный кабинет")
    def click_main_enter_button(self):
        self.click_to_element(Locators.MAIN_ENTER_BUTTON)

    @allure.step(f"Клик по картинке Булка")
    def click_bun_picture(self):
        self.click_to_element(Locators.ROLLS_PICTURE)

    @allure.step("Получение текста игредиентов")
    def get_ingredient_text(self):
        ingredient_text = self.get_text(Locators.ROLLS_SELECT)
        return ingredient_text

    @allure.step(f"Клик по крестику закрытия всплывающего окна")
    def click_close_pop_up_ingredient_button(self):
        self.click_to_element(Locators.CLOSE_POP_UP_BUTTON)

    # @allure.step('Проверить скрытость деталей ингредиентов')
    # def invisibility_ingredient_details(self):
    #     self.element_is_visible(Locators.ROLLS_SELECT)

    @allure.step('Проверить скрытость деталей ингредиентов')
    def check_ingredient_details_invisibility(self):
        return  self.element_is_visible(Locators.ROLLS_SELECT)

    @allure.step(f"Клик по кнопке Начинки")
    def click_filling_button(self):
        self.click_to_element(Locators.FILLING_BUTTON)

    @allure.step(f"видимость кнопки Начинки")
    def filling_button_is_active(self):
        return self.is_button_clickable(Locators.FILLING_BUTTON)

    @allure.step(f"видимость кнопки Начинки")
    def is_filling_button_visible(self):
        return self.get_text(Locators.METER_INGREDIENT)

    @allure.step(f"значение счетчика ингредиентов")
    def get_meter_value(self):
        return self.check_element_is_visibility(Locators.FILLING_BUTTON)



