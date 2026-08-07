import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def pytest_addoption(parser):
    parser.addoption("--browser-name", action="store", default="chrome", help="Browser to use")
    parser.addoption("--headless-type", action="store", default=False, help="Browser Mode")

@pytest.fixture(scope="session")
def browser(request):
    browser = request.config.getoption("--browser-name").lower()
    headless = request.config.getoption("--headless-type")
    if browser == "chrome":
        options = ChromeOptions()
        if not headless:
            options.add_experimental_option("detach", True)
        else:
            options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless=new")
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Browser '{browser}' is not supported.")
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def shared_data():
    return {}

@pytest.fixture(scope="session")
def user_credentials():
    # Read variables injected by GitHub Actions OR local .env
    email = os.getenv("APP_EMAIL")
    password = os.getenv("APP_PASSWORD")
    if not email or not password:
        pytest.fail("Missing credentials! Ensure APP_EMAIL and APP_PASSWORD are set.")
    return {"email": email, "password": password}

# Attach screenshot to pytest-html report on failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver_fixture = item.funcargs.get("driver")
        if driver_fixture:
            os.makedirs("reports/screenshots", exist_ok=True)
            screenshot_path = f"reports/screenshots/{item.name}.png"
            driver_fixture.save_screenshot(screenshot_path)