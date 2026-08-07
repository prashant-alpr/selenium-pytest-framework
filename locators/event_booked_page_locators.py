from selenium.webdriver.common.by import By

class EventBookedPageLocators:

    VIEW_MY_BOOKINGS = (By.XPATH, "//button[text()='View My Bookings']")
    EVENT_BOOKED_NAME = (By.XPATH, "//h3[contains(@class,'font-semibold')]")
    BOOKED_TICKET_COUNT = (By.XPATH, "(//div/span)[6]")
    BOOKED_TICKET_PRICE = (By.XPATH, "//p[contains(@class,'text-xl')]")
    CLEAR_ALL_BOOKINGS = (By.XPATH, "//button[text()='Clear all bookings']")
    NO_BOOKINGS = (By.XPATH, "//h3[contains(@class,'text-lg')]")