import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.event_booked_page import EventBookedPage
#from data.config import CONFIG
from data.event_details import EventDetails

class TestEvents:

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_login(self, browser, user_credentials):
        login_page = LoginPage(browser)
        login_page.load_url(EventDetails.URL)
        #login_page.login(CONFIG.APP_EMAIL, CONFIG.APP_PASSWORD)
        login_page.login(user_credentials.get("email"), user_credentials.get("password"))

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_home_page(self, browser, user_credentials):
        home_page = HomePage(browser)
        home_page.home_page_display(user_credentials.get("email"))
        home_page.logout_display()

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.dependency(depends=["test_home_page"])
    def test_search_event(self, browser):
        home_page = HomePage(browser)
        home_page.click_browse_events()
        home_page.search_event(EventDetails.event)

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.dependency(depends=["test_search_event"])
    def test_event_display(self, browser):
        home_page = HomePage(browser)
        home_page.event_display(EventDetails.event)

    @pytest.mark.regression
    @pytest.mark.dependency(depends=["test_event_display"])
    def test_confirm_booking(self, browser, shared_data):
        home_page = HomePage(browser)
        base_ticket_price = home_page.default_ticket_price()
        home_page.ticket_booking_details(EventDetails.event_username,
                                         EventDetails.event_email, EventDetails.event_phone)
        home_page.increase_ticket_count(1)
        ticket_count = home_page.capture_ticket_count()
        shared_data["ticket_count"] = ticket_count
        actual_ticket_price = home_page.verify_total_ticket_price(base_ticket_price)
        shared_data["actual_ticket_price"] = actual_ticket_price
        home_page.click_on_confirm_booking()

    @pytest.mark.regression
    @pytest.mark.dependency(depends=["test_confirm_booking"])
    def test_view_booking(self, browser, shared_data):
        event_booked_page = EventBookedPage(browser)
        event_booked_page.click_on_view_my_bookings()
        event_booked_page.verify_event_booked_name(EventDetails.event)
        event_booked_page.verify_booked_ticket_count(shared_data.get("ticket_count"))
        event_booked_page.verify_booked_ticket_price(shared_data.get("actual_ticket_price"))

    @pytest.mark.regression
    @pytest.mark.dependency(depends=["test_view_booking"])
    def test_clear_all_bookings(self, browser):
        event_booked_page = EventBookedPage(browser)
        event_booked_page.click_on_clear_all_bookings()
        event_booked_page.verify_no_event_bookings_displayed()
