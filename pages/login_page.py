from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
import logging

logger = logging.getLogger(__name__)

class LoginPage(BasePage):

    def load_url(self, url):
        """ Load the Website """
        logger.info(f"Loading url: {url}")
        self.open_url(url)

    def login(self, email, password):
        """ Login to the Application """
        logger.info(f"Logging in")
        self.type_text(LoginPageLocators.EMAIL_TEXTBOX, email)
        self.type_text(LoginPageLocators.PASSWORD_TEXTBOX, password)
        self.click(LoginPageLocators.LOGIN_BUTTON)



