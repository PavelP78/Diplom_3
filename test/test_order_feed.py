import allure
from pages.order_feed_page import StellarBurgersOrderFeedPage


class TestStellarBurgersOrderFeed:
    @allure.title('Проверка: если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_make_order_authorized_user(self, enter_and_delete_user, driver):
        pages = StellarBurgersOrderFeedPage(driver)
        pages.add_filling_to_order()
        pages.click_order_button()
        details_text = pages.get_order_text()
        assert details_text == "Ваш заказ начали готовить", "Заказ ее принят в работу"

    @allure.title('Проверка: заказы пользователя из раздела '
                  '«История заказов» отображаются на странице «Лента заказов»')
    def test_order_authorized_user_show_in_order_feed(self, enter_and_delete_user, driver):
        pages = StellarBurgersOrderFeedPage(driver)
        pages.add_filling_to_order()
        pages.click_order_button()
        pages.click_close_pop_up_order_button()
        pages.click_authorized_user_personal_account_button()
        pages.click_order_history_button()
        order_history_1_value = pages.get_order_user_number_first_in_order_history()
        pages.click_order_feed_button()
        order_feed_1_value = pages.get_order_user_number_first_in_feed()
        assert order_history_1_value == order_feed_1_value, "Заказы пользователя не отображаются"

    @allure.title('Проверка: при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_order_in_all_time_meter(self, enter_and_delete_user, driver):
        pages = StellarBurgersOrderFeedPage(driver)
        pages.click_order_feed_button()
        order_meter_now = pages.get_value_order_meter_all_time()
        pages.click_design_button()
        pages.add_filling_to_order()
        pages.click_order_button()
        pages.click_close_pop_up_order_button()
        pages.click_order_feed_button()
        order_meter_actually = pages.get_value_order_meter_all_time()
        assert order_meter_actually > order_meter_now, "Ошибка счетчика Выполнено за все время"

    @allure.title('Проверка: при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_order_in_today_meter(self, enter_and_delete_user, driver):
        pages = StellarBurgersOrderFeedPage(driver)
        pages.click_order_feed_button()
        order_meter_now = pages.get_value_order_meter_today()
        pages.click_design_button()
        pages.add_filling_to_order()
        pages.click_order_button()
        pages.click_close_pop_up_order_button()
        pages.click_order_feed_button()
        order_meter_actually = pages.get_value_order_meter_today()
        assert order_meter_actually > order_meter_now, "Ошибка счетчика Выполнено за сегодня"

    @allure.title('Проверка: после оформления заказа его номер появляется в разделе В работе')
    def test_show_order_number_in_progress_area(self, enter_and_delete_user, driver):
        pages = StellarBurgersOrderFeedPage(driver)
        pages.add_filling_to_order()
        pages.click_order_button()
        pages.click_close_pop_up_order_button()
        pages.click_authorized_user_personal_account_button()
        pages.click_order_history_button()
        order_history_1_value = pages.get_order_user_number_first_in_order_history()
        pages.click_order_feed_button()
        actual_meter_value = pages.get_value_order_meter_in_progress_field()
        assert actual_meter_value == order_history_1_value.strip('#'), "Заказ не в работе"
