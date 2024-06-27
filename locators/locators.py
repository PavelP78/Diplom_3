from selenium.webdriver.common.by import By

class StellarBurgersLocators:

    PASSWORD_FIELD = (By.XPATH, '//label[text()="Пароль"]/following::input[1]') # Поле пароль
    EMAIL_FIELD = (By.XPATH, '//label[text()="Email"]/following::input[1]') # Поле е-майл
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//nav/a[@class='AppHeader_header__link__3D_hX']") # Кнопка личный кабинет авторизиованного пользователя
    ENTER_BUTTON = (By.XPATH, '//button[text()="Войти"]') # Кнопка войти
    MAIN_ENTER_BUTTON = (By.XPATH, '//button[text()="Войти в аккаунт"]') # Кнопка войти в аккаунт на главной
    ENTER_BUTTON_REGISTRATION_FORM = (By.XPATH, '//a[text()="Войти"]') # Кнопка войти  в форме регистрации
    BUTTON_PASSWORD_RECOVERY_FORM = (By.XPATH, '//a[text()="Восстановить пароль"]') # Кнопка  восстановления пароля
    ENTER_BUTTON_PASSWORD_RECOVERY_FORM = (By.XPATH, '//a[text()="Войти"]') # Кнопка войтив форме восстановления пароля
    REGISTRATION_BUTTON = (By.XPATH, '//a[text()="Зарегистрироваться"]') # Кнопка зарегистрироваться
    DESIGNER_BUTTON = (By.XPATH, '//p[text()="Конструктор"]') # Кнопка конструктор
    LOGO_BUTTON = (By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]') # Логотип Stellar Burgers
    EXIT_BUTTON = (By.XPATH, '//button[text()="Выход"]') # Кнопка «Выход» в личном кабинете
    ROLLS_BUTTON = (By.XPATH, '//span[text()="Булки"]') # Кнопка «Булки»
    SOUCE_BUTTON = (By.XPATH, '//span[text()="Соусы"]') # Кнопка «Соусы»
    FILLING_BUTTON = (By.XPATH, '//span[text()="Начинки"]') # Кнопка «Начинки»
    ENTER_BUTTON_ACCOUNT = (By.XPATH, '//button[text()="Войти в аккаунт"]') # Кнопка войти в аккаунт
    ERROR_PASSWORD= (By.XPATH, '//p[text()="Некорректный пароль"]') # Надпись некорректный пароль
    ORDER_BUTTON= (By.XPATH, '//button[text()="Оформить заказ"]') # Кнопка оформить заказ
    NAME_FIELD = (By.XPATH, '//label[text()="Имя"]/following::input[1]') # Поле имя при регистрации
    EMAIL_FIELD_REGISTRATION = (By.XPATH, '//label[text()="Email"]/following::input[1]') # Поле е-майл при регистрации
    PASSWORD_FIELD_REGISTRATION = (By.XPATH, '//label[text()="Пароль"]/following::input[1]') # Поле пароль при регистрации
    REGISTRATION_BUTTON_REGISTRATION = (By.XPATH, '//button[text()="Зарегистрироваться"]') # Кнопка зарегистрироваться на странице регистрации
    ERROR_PASSWORD_REGISTRATION= (By.XPATH, '//p[text()="Некорректный пароль"]') # Надпись некорректный пароль на странице регистрации
    ROLLS_PICTURE = (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]') # Картинка флюоресцентная булка
    ROLLS_SELECT = (By.XPATH, '//h2[text()="Детали ингредиента"]') # Меню булки после клика на Булки
    CURRENT_TAB = (By.XPATH, '//div[contains(@class, "current")]/span') # Путь элементов с классом содержащих  current
    SOUCE_PICTURE = (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa72"]') # Картинка соус Spisy-x
    FILLING_PICTURE = (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa70"]') # Картинка начинки говяжий метеорит
    SAVE_BUTTON= (By.XPATH, '//button[text()="Сохранить"]') # Кнопка сохранить
    EMAIL_FIELD_RECOVERY_PASSWORD = (By.XPATH, '//label[text()="Email"]/following-sibling::input')  # Поле е-майл при восстановлении пароля
    SHOW_PASSWORD_BUTTON = By.XPATH, '//div[contains(@class,"icon-action")]'  # Kнопка Показать пароль
    ACTIVE_PASSWORD_FIELD = (By.XPATH, '//label[contains(@class,"input__placeholder-focused")]') # Поле ввода пароля после нажатия кнопки показать пароль - активно
    ORDER_HISTORY_BUTTON = (By.LINK_TEXT, 'История заказов')  # Кнопка "История заказов" в личном кабинете
    ORDER_FEED_BUTTON = (By.XPATH, '//p[text()="Лента Заказов"]/parent::a')  # Кнопка "Лента заказов"
    CLOSE_POP_UP_BUTTON = By.XPATH, '//button[contains(@class,"close")]'  # закрытие всплывающего окна деталей ингредиента
    METER_INGREDIENT = (By.XPATH, '//ul[1]/a[1]//p[contains(@class, "num")]')  # Счетчик ингредиентов
    ORDER_BASKET_UP = (By.XPATH, "//span[@class='constructor-element__text' and text()='Перетяните булочку сюда (верх)']") # Счетчик ингредиентов

# class StellarBurgersLocatorsMainPage:
#     MAIN_ENTER_BUTTON = (By.XPATH, '//button[text()="Войти в аккаунт"]') # Кнопка войти в аккаунт на главной
#
#
#
# class StellarBurgersLocatorsOrder:
