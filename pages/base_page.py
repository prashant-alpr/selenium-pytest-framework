import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

logger = logging.getLogger(__name__)

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open_url(self, url):
        logger.info(f"Navigating to URL: {url}")
        self.driver.get(url)

    def find(self, locator):
        logger.info(f"Finding element: {locator}")
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        logger.info(f"Clicking on element: {locator}")
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def type_text(self, locator, text):
        logger.info(f"Typing {text} in locator: {locator}")
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        logger.info(f"Getting text from locator: {locator}")
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text.strip()

    def is_visible(self, locator):
        logger.info(f"Visibility check of {locator}")
        try:
            return bool(self.wait.until(EC.visibility_of_element_located(locator)))
        except TimeoutException:
            return False
        except NoSuchElementException:
            return False

    def alert_accept(self):
        logger.info(f"Accepting the alert")
        self.driver.switch_to.alert.accept()

    def java_script_element_click(self, locator):
        logger.info(f"Clicking on element through Java Script executor: {locator}")
        self.driver.execute_script(f"document.getElementById({locator}).click();")


