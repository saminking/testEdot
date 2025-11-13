from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class BasePage:
    def __init__(self, driver, base_url=None):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.base_url = base_url

    def open(self, path="/"):
        url = (self.base_url.rstrip("/") if self.base_url else "").strip()
        self.driver.get(f"{url}{path}")

    def click(self, by_locator):
        element = self.wait.until(EC.element_to_be_clickable(by_locator))
        element.click()
    
    def type(self, by_locator, text):
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        element.clear()
        element.send_keys(text)
    
    def upload_file(self, by_locator, file_path):
        element = self.wait.until(EC.presence_of_element_located(by_locator))
        element.send_keys(file_path)
    
    def text_of(self, by_locator):
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        return element.text
    
    def attribute_of(self, by_locator, attribute):
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        return element.get_attribute(attribute)
    
    def select_from_dropdown(self, by_locator, value):
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        element.click()
        target_dropdown = self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//span[.='{value}']")))
        target_dropdown.click()

    def select_from_dropdown_location(self, by_locator, value):
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        element.click()
        target_dropdown = self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//div[.='{value}']")))
        target_dropdown.click()
    
    def scroll_down(self):
        element = self.driver.find_element(By.TAG_NAME, "body")
        element.send_keys(Keys.END)
    
    def sleep(self, seconds):
        time.sleep(seconds)
    
    def page_refresh(self):
        self.driver.refresh()

    def exist(self, by_locator):
        try:
            self.wait.until(EC.presence_of_element_located(by_locator))
            return True
        except:
            return False
