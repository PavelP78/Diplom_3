import allure
from pages.order_feed_page import StellarBurgersOrderFeedPage


class TestStellarBurgersOrderFeed:
    @allure.title('Проверка: если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_make_order_authorized_user(self, driver):
        pages = StellarBurgersOrderFeedPage(driver)
        pages.click_main_enter_button()
        pages.send_keys_to_placeholder_email()
        pages.send_keys_to_placeholder_password()
        pages.click_enter_button()
        pages.add_filling_to_order()
        pages.click_order_button()
        details_text = pages.get_order_text()
        assert details_text == "Ваш заказ начали готовить"

    @allure.title('Проверка: заказы пользователя из раздела '
                  '«История заказов» отображаются на странице «Лента заказов»')
    def test_order_authorized_user_show_in_order_feed(self, driver):
        pages = StellarBurgersOrderFeedPage(driver)
        pages.click_main_enter_button()
        pages.send_keys_to_placeholder_email()
        pages.send_keys_to_placeholder_password()
        pages.click_enter_button()
        pages.add_filling_to_order()
        pages.click_order_button()
        pages.click_close_pop_up_order_button()
        pages.click_authorized_user_personal_account_button()
        pages.click_order_history_button()
        order_history_1_value = pages.get_order_user_number_first_in_order_history()
        pages.click_order_feed_button()
        order_feed_1_value = pages.get_order_user_number_first_in_feed()
        print(order_feed_1_value)
        print(order_history_1_value)
        assert order_history_1_value == order_feed_1_value

    @allure.title('Проверка: при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_order_in_all_time_meter(self, driver):
        pages = StellarBurgersOrderFeedPage(driver)
        pages.click_main_enter_button()
        pages.send_keys_to_placeholder_email()
        pages.send_keys_to_placeholder_password()
        pages.click_enter_button()
        pages.click_order_feed_button()
        order_meter_now = pages.get_value_order_meter_all_time()
        pages.click_design_button()
        pages.add_filling_to_order()
        pages.click_order_button()
        pages.click_close_pop_up_order_button()
        pages.click_order_feed_button()
        order_meter_actually = pages.get_value_order_meter_all_time()
        print(order_meter_actually)
        print(order_meter_now)
        assert order_meter_actually > order_meter_now

    @allure.title('Проверка: при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_order_in_today_meter(self, driver):
        pages = StellarBurgersOrderFeedPage(driver)
        pages.click_main_enter_button()
        pages.send_keys_to_placeholder_email()
        pages.send_keys_to_placeholder_password()
        pages.click_enter_button()
        pages.click_order_feed_button()
        order_meter_now = pages.get_value_order_meter_today()
        pages.click_design_button()
        pages.add_filling_to_order()
        pages.click_order_button()
        pages.click_close_pop_up_order_button()
        pages.click_order_feed_button()
        order_meter_actually = pages.get_value_order_meter_today()
        print(order_meter_now)
        print(order_meter_actually)
        assert order_meter_actually == order_meter_now

    @allure.title('Проверка: после оформления заказа его номер появляется в разделе В работе')
    def test_show_order_number_in_progress_area(self, driver):
        pages = StellarBurgersOrderFeedPage(driver)
        pages.click_main_enter_button()
        pages.send_keys_to_placeholder_email()
        pages.send_keys_to_placeholder_password()
        pages.click_enter_button()
        pages.add_filling_to_order()
        pages.click_order_button()
        pages.click_close_pop_up_order_button()
        pages.click_authorized_user_personal_account_button()
        pages.click_order_history_button()
        order_history_1_value = pages.get_order_user_number_first_in_order_history()
        pages.click_order_feed_button()
        actual_meter_value = pages.get_value_order_meter_in_progress_field()
        print(actual_meter_value)
        print(order_history_1_value)
        assert actual_meter_value == order_history_1_value.strip('#')
