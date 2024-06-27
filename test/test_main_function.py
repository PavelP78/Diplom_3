from data import StellarBurgersUrl as Url
import allure
from pages.main_function_page import StellarBurgersMainFunctionPage


class TestStellarBurgersMainFunction:
    @allure.title('Проверка: переход по клику на «Лента заказов»')
    def test_order_feed_button_click(self, driver):
        pages = StellarBurgersMainFunctionPage(driver)
        pages.click_order_feed_button()
        assert driver.current_url == f'{Url.URL_ORDER_FEED}', "Url is wrong"

    @allure.title('Проверка: переход по клику на «Конструктор»')
    def test_design_button_click(self, driver):
        pages = StellarBurgersMainFunctionPage(driver)
        pages.click_main_enter_button()
        pages.click_design_button()
        assert driver.current_url == f'{Url.URL_MAIN}', "Url is wrong"

    @allure.title('Проверка: если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_ingredient_pop_up(self, driver):
        pages = StellarBurgersMainFunctionPage(driver)
        pages.click_bun_picture()
        details_text = pages.get_ingredient_text()
        assert details_text == "Детали ингредиента"

    @allure.title('Проверка: если кликнуть на ингредиент, появится всплывающее окно с деталями '
                  'которое закрывается кликом по крестику')
    def test_ingredient_pop_up_close(self, driver):
        pages = StellarBurgersMainFunctionPage(driver)
        pages.click_bun_picture()
        pages.click_close_pop_up_ingredient_button()
        assert pages.is_filling_button_visible() is True

    @allure.title('Проверка: при добавлении ингредиента в заказ'
                  ' счётчик этого ингридиента увеличивается')
    def test_add_ingredient_to_basket(self, driver):
        pages = StellarBurgersMainFunctionPage(driver)
        pages.click_bun_picture()
        pages.click_close_pop_up_ingredient_button()
        assert pages.is_filling_button_visible() is True
