from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class StellarBurgerBasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator):
        element_to_click = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        WebDriverWait(self.driver, 10).until(EC.visibility_of(element_to_click))
        element_to_click.click()

    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))

    def click_to_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        self.find_element(locator).click()

    def get_text(self, locator):
        return self.find_element(locator).text

    def get_actually_text(self, locator):
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
            actually_text = self.driver.find_element(*locator).text
            return actually_text

    def set_text(self, locator, text):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).send_keys(text)

    def tab_switch(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def get_url(self):
        return self.driver.current_url

    def open_url(self, url):
        return self.driver.get(url)

    def element_is_visible(self, locator):
        try:
            element = self.find_element(locator)
            return element.is_displayed()
        except NoSuchElementException:
            return False
        except AttributeError:
            return False

    def is_button_clickable(self, locator):

        try:
            button = self.driver.find_element(*locator)
            if button.is_enabled() and button.is_displayed():
                return True
            else:
                return False
        except NoSuchElementException:
            return False

    def check_element_is_visibility(self, locator):
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    def drag_and_drop_element(self, locator_1, locator_2):
        drag = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator_1))
        drop = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator_2))
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(drag, drop).perform()
