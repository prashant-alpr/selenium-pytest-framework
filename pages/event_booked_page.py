from pages.base_page import BasePage
from locators.event_booked_page_locators import EventBookedPageLocators
import re
import logging

logger = logging.getLogger(__name__)

class EventBookedPage(BasePage):

    def click_on_view_my_bookings(self):
        """ Click on View My Bookings button """
        logger.info("Click on View My Bookings button")
        self.click(EventBookedPageLocators.VIEW_MY_BOOKINGS)

    def verify_event_booked_name(self, event):
        """ Verify event booked name """
        booked_event_name = self.get_text(EventBookedPageLocators.EVENT_BOOKED_NAME)
        logger.info(f"Event booked name: {booked_event_name}")
        assert booked_event_name == event, "Event name is not correct"

    def verify_booked_ticket_count(self, ticket_count):
        """ Verify event booked ticket count """
        booked_ticket_count = self.get_text(EventBookedPageLocators.BOOKED_TICKET_COUNT)
        booked_ticket_count = re.search(r"\d+", booked_ticket_count).group()
        logger.info(f"Event booked ticket count: {booked_ticket_count}")
        assert booked_ticket_count == ticket_count, "Ticket count is not correct"

    def verify_booked_ticket_price(self, ticket_price):
        """ Verify event booked ticket price """
        booked_ticket_price = self.get_text(EventBookedPageLocators.BOOKED_TICKET_PRICE)
        logger.info(f"Event booked ticket price: {booked_ticket_price}")
        assert booked_ticket_price == ticket_price, "Price is not correct"

    def click_on_clear_all_bookings(self):
        """ Click on Clear All Bookings button """
        logger.info("Click on Clear All Bookings button")
        self.click(EventBookedPageLocators.CLEAR_ALL_BOOKINGS)
        self.alert_accept()

    def verify_no_event_bookings_displayed(self):
        """ Verify no event bookings are displayed """
        no_bookings = self.get_text(EventBookedPageLocators.NO_BOOKINGS)
        logger.info(f"No event bookings displayed: {no_bookings}")
        assert no_bookings == "No bookings yet", "Bookings is not correct"