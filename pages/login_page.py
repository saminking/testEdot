import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    BUTTON_INPUT_EMAIL = (By.XPATH, "//button[text()='Use Email or Username']")
    INPUT_EMAIL = (By.XPATH, "//input[@name ='username']")
    LOGIN_USERNAME = (By.XPATH, "//button[text()='Log In']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    LOGIN_PASSWORD = (By.XPATH, "//button[@type='submit']")
    BERANDA_DASHBOARD = (By.XPATH, "//a[text()='Home']")

    @allure.step("Open Login Page")
    def open_login(self):
        self.open("/")

    
    @allure.step("Perform Login")
    def login(self, email, password):
        self.click(self.BUTTON_INPUT_EMAIL)
        self.type(self.INPUT_EMAIL, email)
        self.click(self.LOGIN_USERNAME)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_PASSWORD)

    @allure.step("Assert Logged In")
    def assert_logged_in(self):
        assert self.exist(self.BERANDA_DASHBOARD), "Login failed - Beranda dashboard not found"

