from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators
import logging

logger = logging.getLogger(__name__)

class HomePage(BasePage):

    def home_page_display(self, email):
        """ Verify User Email is displayed in Home Page """
        user_email = self.get_text(HomePageLocators.EMAIL_DISPLAY)
        logger.info(f"User Email: {user_email}")
        assert user_email == email, "User Email is not correct"

    def logout_display(self):
        """ Verify Logout button is displayed in Home Page """
        self.is_visible(HomePageLocators.LOGOUT_BUTTON)
        logout_text = self.get_text(HomePageLocators.LOGOUT_BUTTON)
        logger.info(f"Logout Button: {logout_text}")
        assert logout_text == "Logout", "Logout text is not correct"

    def click_browse_events(self):
        """ Click on Browse Events"""
        logger.info("Clicking Browse Events")
        self.click(HomePageLocators.BROWSE_EVENTS)

    def search_event(self, event):
        """ Search for Event """
        logger.info(f"Searching for event: {event}")
        self.is_visible(HomePageLocators.SEARCH_BOX)
        self.type_text(HomePageLocators.SEARCH_BOX, event)

    def event_display(self, event):
        """ Verify Event is displayed in Home Page """
        event_name = self.get_text(HomePageLocators.EVENT_NAME)
        assert event_name == event, "Event name is not correct"
        logger.info(f"Event name: {event_name}")
        self.click(HomePageLocators.BOOK_NOW)

    def default_ticket_price(self):
        """ Return default ticket price """
        base_ticket_price = self.get_text(HomePageLocators.BASE_TICKET)
        logger.info(f"Default ticket price: {base_ticket_price}")
        return base_ticket_price

    def ticket_booking_details(self, username, email, phone_no):
        """ Enter Ticket Booking Details """
        logger.info(f"Enter Ticket Booking Details: {username}, {email}, {phone_no}")
        self.type_text(HomePageLocators.EVENT_USERNAME, username)
        self.type_text(HomePageLocators.EVENT_EMAIL, email)
        self.type_text(HomePageLocators.EVENT_PHONE, phone_no)

    def increase_ticket_count(self, count):
        """ Increase Ticket Count """
        logger.info(f"Increase Ticket Count: {count}")
        for _ in range(count):
            self.click(HomePageLocators.TICKET_COUNT_PLUS)

    def capture_ticket_count(self):
        """ Return Ticket Count """
        ticket_count = self.get_text(HomePageLocators.TICKET_COUNT)
        logger.info(f"Captured Ticket Count: {ticket_count}")
        return ticket_count

    def verify_total_ticket_price(self, base_ticket):
        """ Verify Total Ticket Price and return the same """
        actual_ticket_price = self.get_text(HomePageLocators.ACTUAL_TICKET_PRICE)
        logger.info(f"Actual ticket price: {actual_ticket_price}")
        base_amount = str(int(base_ticket[1:]) * 2)
        base_amount = f"{base_ticket[0]}{base_amount}"
        logger.info(f"Base ticket amount: {base_amount}")
        assert actual_ticket_price == base_amount, "Calculated amount is not correct"
        return actual_ticket_price

    def click_on_confirm_booking(self):
        """ Click on Confirm Booking """
        logger.info(f"Click on Confirm Booking")
        self.java_script_element_click(HomePageLocators.CONFIRM_BOOKING)





