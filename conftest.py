import os
import pytest
import allure  
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage

def pytest_addoption(parser):
    parser.addoption("--base-url", action="store", default=None, help="Base URL for eSuite")
    parser.addoption("--email", action="store", default=None, help="email for login eSuite")
    parser.addoption("--password", action="store", default=None, help="password for login eSuite")
    parser.addoption("--headless", action="store", default=None, help="Run browser in headless mode (true|false)")

@pytest.fixture(scope="session")
def config(pytestconfig):
    load_dotenv()
    _headless_opt = pytestconfig.getoption("headless")
    if isinstance(_headless_opt, bool):
        _headless = _headless_opt
    else:
        _headless = str(_headless_opt or os.getenv("HEADLESS", "False")).lower() == "true"

    _password_opt = pytestconfig.getoption("password")
    _password = _password_opt or os.getenv("ESUITE_PASSWORD")
    if not _password:
        raise pytest.UsageError("Password must be provided via --password or the ESUITE_PASSWORD environment variable")
    _base_url_opt = pytestconfig.getoption("base_url")
    _base_url = _password_opt or os.getenv("BASE_URL")
    if not _base_url:
        raise pytest.UsageError("Base URL must be provided via --base_url or the BASE_URL environment variable")
    _email_opt = pytestconfig.getoption("email")
    _email = _email_opt or os.getenv("ESUITE_EMAIL")
    if not _email:
        raise pytest.UsageError("Email must be provided via --email or the ESUITE_EMAIL environment variable")

    return {
        "base_url": _base_url,
        "email": _email,
        "password": _password,
        "headless": _headless,
    }

@pytest.fixture
def driver(config):
    options = Options()
    if config["headless"]:
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1440,900")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage") 
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    yield driver
    try:
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
        allure.attach(driver.page_source, name="page_source", attachment_type=allure.attachment_type.HTML)
    except Exception :
        pass
    driver.quit()

@pytest.fixture(scope="class")
def driver(config):
    options = Options()
    if config["headless"]:
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1440,900")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage") 
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    yield driver
    try:
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
        allure.attach(driver.page_source, name="page_source", attachment_type=allure.attachment_type.HTML)
    except Exception :
        pass
    driver.quit()

@pytest.fixture(scope="class")
def login_before_class(driver_class, config):
    login_page = LoginPage(driver_class, base_url=config["base_url"])
    login_page.open_login()
    login_page.login(config["email"], config["password"])
    login_page.assert_logged_in()
    return driver_class

@pytest.fixture
def shot(request):
    driver = None
    for name in ("driver", "driver_class"):
        try:
            driver = request.getfixturevalue(name)
            if driver:
                break
        except Exception:
            pass

    def _snap(name="screenshot"):
        if driver:
            png = driver.get_screenshot_as_png()
            allure.attach(png, name=name, attachment_type=allure.attachment_type.PNG)
    return _snap

