from selenium.webdriver.common.by import By

class HomePageLocators:

    EMAIL_DISPLAY = (By.ID, "user-email-display")
    LOGOUT_BUTTON = (By.ID, "logout-btn")
    BROWSE_EVENTS = (By.XPATH, "//span[text()='Browse Events →']")
    SEARCH_BOX = (By.XPATH, "//input[contains(@placeholder,'Search events')]")
    EVENT_NAME = (By.XPATH, "//div[contains(@class,'p-4')]/a/h3")
    BOOK_NOW = (By.ID, "book-now-btn")
    BASE_TICKET = (By.XPATH, "//span[contains(@class,'text-2xl')]")
    EVENT_USERNAME = (By.ID, "customerName")
    EVENT_EMAIL = (By.ID, "customer-email")
    EVENT_PHONE = (By.ID, "phone")
    TICKET_COUNT_PLUS = (By.XPATH, "//button[text()='+']")
    TICKET_COUNT = (By.ID, "ticket-count")
    ACTUAL_TICKET_PRICE = (By.XPATH, "//span[@class='text-indigo-700']")
    CONFIRM_BOOKING = (By.ID, "confirm-booking")