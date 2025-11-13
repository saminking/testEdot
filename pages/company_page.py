import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage

class CompanyPage(BasePage):
    BUTTON_ADD_NEW_COMPANY = (By.XPATH, "//button[contains(text(),'+ ')]")
    TEXT_BOX_COMPANY_NAME = (By.XPATH, "//input[@placeholder = 'Input Company Name']")
    TEXT_BOX_EMAIL_COMPANY = (By.XPATH, "//input[@placeholder = 'Input Email']")
    TEXT_BOX_PHONE_COMPANY = (By.XPATH, "//input[@placeholder = 'Input Phone']")
    TEXT_BOX_ADDRESS_COMPANY = (By.XPATH, "//input[@placeholder = 'Input Address']")
    DROPDOWN_INDUSTRY = (By.XPATH, "//span[text()='Choose Industry Type']")
    DROPDOWN_COMPANY_TYPE = (By.XPATH, "//span[text()='Choose Company Type']")
    DROPDOWN_LANGUAGE = (By.XPATH, "//span[text()='Choose Language']") 
    DROPDOWN_COUNTRY = (By.XPATH, "//span[text()='Choose Country']")
    DROPDOWN_PROVINCE = (By.XPATH, "//span[text()='Choose Province']")
    DROPDOWN_CITY = (By.XPATH, "//span[text()='Choose City']")
    DROPDOWN_DISTRICT = (By.XPATH, "//span[text()='Choose District']")
    DROPDOWN_SUBDISTRICT = (By.XPATH, "//span[text()='Choose Sub District']")

    BUTTON_NEXT_PAGE = (By.XPATH, "//button[contains(text(),'Next')]")
    BUTTON_ADD_DOCUMENT = (By.XPATH, "//button[contains(text(),'+ Add Document')]")

    DROPDOWN_DOCUMENT = (By.XPATH, "//span[text()='Choose Legal Document']")
    UPLOAD_DOCUMENT_INPUT = (By.XPATH, "//input[@type='file']")
    BUTTON_SUBMIT_DOCUMENT = (By.XPATH, "//button[contains(text(),'Submit Document')]")

    BUTTON_AUTOFILL_BRANCH_OFFICE = (By.XPATH, "//button[contains(text(),'Fill in with the same data from the Company records')]")
    BUTTON_CHECKBOX_TNC = (By.XPATH, "//button[@role='checkbox']")
    BUTTON_REGISTER_COMPANY = (By.XPATH, "//button[contains(text(),'Register')]")
    TEXT_BOX_BRANCH_OFFICE_NAME = (By.XPATH, "//input[@placeholder='Input Branch Name']")

    TEXT_BOX_COMPANY_NAME_DETAIL = (By.XPATH, "//input[@placeholder='Input Company Name']")

    def get_company_name_locator(self, company_name):
        return (By.XPATH, f"//div[contains(text(), '{company_name}')]/parent::div/following-sibling::div/div/button[contains(text(), 'Manage')]")

    @allure.step("Open Company Form")
    def open_company_form(self):
        self.click(self.BUTTON_ADD_NEW_COMPANY)

    @allure.step("Fill Company Basic Info")
    def fill_company_basic_info(self, name, email, phone, industry, company_type, language, country, province, city, district, subdistrict, address):
        self.type(self.TEXT_BOX_COMPANY_NAME, name)
        self.type(self.TEXT_BOX_EMAIL_COMPANY, email)
        self.type(self.TEXT_BOX_PHONE_COMPANY, phone)
        self.type(self.TEXT_BOX_ADDRESS_COMPANY, address)
        self.select_from_dropdown(self.DROPDOWN_INDUSTRY, industry)
        self.select_from_dropdown(self.DROPDOWN_COMPANY_TYPE, company_type)
        self.select_from_dropdown(self.DROPDOWN_LANGUAGE, language)
        self.select_from_dropdown(self.DROPDOWN_COUNTRY, country)
        self.select_from_dropdown_location(self.DROPDOWN_PROVINCE, province)
        self.select_from_dropdown_location(self.DROPDOWN_CITY, city)
        self.select_from_dropdown_location(self.DROPDOWN_DISTRICT, district)
        self.select_from_dropdown_location(self.DROPDOWN_SUBDISTRICT, subdistrict)
        self.click(self.BUTTON_NEXT_PAGE)
    
    @allure.step("Upload Company Document")
    def upload_company_document(self, document_type, file_path):
        self.click(self.BUTTON_ADD_DOCUMENT)
        self.select_from_dropdown_location(self.DROPDOWN_DOCUMENT, document_type)
        self.upload_file(self.UPLOAD_DOCUMENT_INPUT, file_path)
        self.click(self.BUTTON_SUBMIT_DOCUMENT)
        self.click(self.BUTTON_NEXT_PAGE)
    
    @allure.step("Register Company")
    def register_company(self, branch_name):
        self.type(self.TEXT_BOX_BRANCH_OFFICE_NAME, branch_name)
        self.click(self.BUTTON_AUTOFILL_BRANCH_OFFICE)
        self.click(self.BUTTON_CHECKBOX_TNC)
        self.click(self.BUTTON_REGISTER_COMPANY)
        self.exist(self.BUTTON_ADD_NEW_COMPANY)

    @allure.step("Verify Company Created")
    def verify_company_created(self, company_name):
        company_locator = self.get_company_name_locator(company_name)
        self.scroll_down()
        self.sleep(10)
        self.click(company_locator)
        company_name_in_detail = self.attribute_of(self.TEXT_BOX_COMPANY_NAME_DETAIL, "value")
        print (company_name_in_detail)
        assert company_name_in_detail == company_name, f"Company name mismatch: expected {company_name}, got {company_name_in_detail}"









