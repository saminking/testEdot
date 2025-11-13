import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage


class DashboardPage(BasePage):
    MENU_COMPANY = (By.XPATH, "//div/child::a[contains(text(), 'Companies')]")


    @allure.step("Go to Company module")
    def goto_company(self):
        self.click(self.MENU_COMPANY)