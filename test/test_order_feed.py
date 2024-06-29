import allure
from pages.order_feed_page import StellarBurgersOrderFeedPage
from api_page import StellarBurgersAPI


class TestStellarBurgersOrderFeed:
    @allure.title('Проверка: если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_make_order_authorized_user(self, driver):
        stellar_burgers_api = StellarBurgersAPI()
        sign_up_data = stellar_burgers_api.sign_up_data
        new_user_response = stellar_burgers_api.create_new_user(sign_up_data)
        access_token = stellar_burgers_api.get_access_token(new_user_response)
        assert new_user_response.status_code == 200, "Новый пользователь не создан"
        pages = StellarBurgersOrderFeedPage(driver)
        pages.click_main_enter_button()
        pages.send_keys_to_placeholder_email(stellar_burgers_api)
        pages.send_keys_to_placeholder_password(stellar_burgers_api)
        pages.click_enter_button()
        pages.add_filling_to_order()
        pages.click_order_button()
        details_text = pages.get_order_text()
        assert details_text == "Ваш заказ начали готовить", "Заказ ее принят в работу"
        response = stellar_burgers_api.delete_user(access_token)
        assert response.status_code == 202, "Пользователь не удален"

    @allure.title('Проверка: заказы пользователя из раздела '
                  '«История заказов» отображаются на странице «Лента заказов»')
    def test_order_authorized_user_show_in_order_feed(self, driver):
        stellar_burgers_api = StellarBurgersAPI()
        sign_up_data = stellar_burgers_api.sign_up_data
        new_user_response = stellar_burgers_api.create_new_user(sign_up_data)
        access_token = stellar_burgers_api.get_access_token(new_user_response)
        assert new_user_response.status_code == 200, "Новый пользователь не создан"
        pages = StellarBurgersOrderFeedPage(driver)
        pages.click_main_enter_button()
        pages.send_keys_to_placeholder_email(stellar_burgers_api)
        pages.send_keys_to_placeholder_password(stellar_burgers_api)
        pages.click_enter_button()
        pages.add_filling_to_order()
        pages.click_order_button()
        pages.click_close_pop_up_order_button()
        pages.click_authorized_user_personal_account_button()
        pages.click_order_history_button()
        order_history_1_value = pages.get_order_user_number_first_in_order_history()
        pages.click_order_feed_button()
        order_feed_1_value = pages.get_order_user_number_first_in_feed()
        assert order_history_1_value == order_feed_1_value, "Заказы пользователя не отображаются"
        response = stellar_burgers_api.delete_user(access_token)
        assert response.status_code == 202, "Пользователь не удален"

    @allure.title('Проверка: при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_order_in_all_time_meter(self, driver):
        stellar_burgers_api = StellarBurgersAPI()
        sign_up_data = stellar_burgers_api.sign_up_data
        new_user_response = stellar_burgers_api.create_new_user(sign_up_data)
        access_token = stellar_burgers_api.get_access_token(new_user_response)
        assert new_user_response.status_code == 200, "Новый пользователь не создан"
        pages = StellarBurgersOrderFeedPage(driver)
        pages.click_main_enter_button()
        pages.send_keys_to_placeholder_email(stellar_burgers_api)
        pages.send_keys_to_placeholder_password(stellar_burgers_api)
        pages.click_enter_button()
        pages.click_order_feed_button()
        order_meter_now = pages.get_value_order_meter_all_time()
        pages.click_design_button()
        pages.add_filling_to_order()
        pages.click_order_button()
        pages.click_close_pop_up_order_button()
        pages.click_order_feed_button()
        order_meter_actually = pages.get_value_order_meter_all_time()
        assert order_meter_actually > order_meter_now, "Ошибка счетчика Выполнено за все время"
        response = stellar_burgers_api.delete_user(access_token)
        assert response.status_code == 202, "Пользователь не удален"

    @allure.title('Проверка: при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_order_in_today_meter(self, driver):
        stellar_burgers_api = StellarBurgersAPI()
        sign_up_data = stellar_burgers_api.sign_up_data
        new_user_response = stellar_burgers_api.create_new_user(sign_up_data)
        access_token = stellar_burgers_api.get_access_token(new_user_response)
        assert new_user_response.status_code == 200, "Новый пользователь не создан"
        pages = StellarBurgersOrderFeedPage(driver)
        pages.click_main_enter_button()
        pages.send_keys_to_placeholder_email(stellar_burgers_api)
        pages.send_keys_to_placeholder_password(stellar_burgers_api)
        pages.click_enter_button()
        pages.click_order_feed_button()
        order_meter_now = pages.get_value_order_meter_today()
        pages.click_design_button()
        pages.add_filling_to_order()
        pages.click_order_button()
        pages.click_close_pop_up_order_button()
        pages.click_order_feed_button()
        order_meter_actually = pages.get_value_order_meter_today()
        assert order_meter_actually > order_meter_now, "Ошибка счетчика Выполнено за сегодня"
        response = stellar_burgers_api.delete_user(access_token)
        assert response.status_code == 202, "Пользователь не удален"

    @allure.title('Проверка: после оформления заказа его номер появляется в разделе В работе')
    def test_show_order_number_in_progress_area(self, driver):
        stellar_burgers_api = StellarBurgersAPI()
        sign_up_data = stellar_burgers_api.sign_up_data
        new_user_response = stellar_burgers_api.create_new_user(sign_up_data)
        access_token = stellar_burgers_api.get_access_token(new_user_response)
        assert new_user_response.status_code == 200, "Новый пользователь не создан"
        pages = StellarBurgersOrderFeedPage(driver)
        pages.click_main_enter_button()
        pages.send_keys_to_placeholder_email(stellar_burgers_api)
        pages.send_keys_to_placeholder_password(stellar_burgers_api)
        pages.click_enter_button()
        pages.add_filling_to_order()
        pages.click_order_button()
        pages.click_close_pop_up_order_button()
        pages.click_authorized_user_personal_account_button()
        pages.click_order_history_button()
        order_history_1_value = pages.get_order_user_number_first_in_order_history()
        pages.click_order_feed_button()
        actual_meter_value = pages.get_value_order_meter_in_progress_field()
        assert actual_meter_value == order_history_1_value.strip('#'), "Заказ не в работе"
        response = stellar_burgers_api.delete_user(access_token)
        assert response.status_code == 202, "Пользователь не удален"
