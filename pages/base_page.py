from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains


class StellarBurgerBasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))

    def click_to_element(self, locator):
        self.find_element(locator).click()

    def get_text(self, locator):
        return self.find_element(locator).text
    
    def get_actually_text(self, locator):
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
        drag = self.driver.find_element(*locator_1)
        drop = self.driver.find_element(*locator_2)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(drag, drop).perform()
    