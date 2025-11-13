import allure
from faker import Faker
from pages.login_page import LoginPage 
from pages.home_page import DashboardPage
from pages.company_page import CompanyPage
from pathlib import Path

fake = Faker("id_ID")
resource_dir = Path(__file__).parent / "resources"   # tests/resources
file_path = (resource_dir / "example_img.jpg").resolve()
assert file_path.exists(), f"Upload file not found: {file_path}"


@allure.feature("Company")
@allure.story("Create Company")
@allure.severity(allure.severity_level.CRITICAL)
class TestCreateCompany:
    @allure.title("Create New Company and Verify its details")
    def test_create_company(self, driver, config, shot):
        login = LoginPage(driver, base_url=config["base_url"])
        login.open_login()
        login.login(config["email"], config["password"])
        login.assert_logged_in()
        shot("logged in")

        dashboard = DashboardPage(driver, base_url=config["base_url"])
        dashboard.goto_company()
        shot("navigated to company module")

        company_page = CompanyPage(driver, base_url=config["base_url"])
        company_page.open_company_form()
        shot("opened company form")
        company_name = fake.company()
        company_email = fake.company_email()
        company_phone = fake.phone_number() 
        company_address = fake.address().replace("\n", ", ")
        company_page.fill_company_basic_info(
            name=company_name,
            email=company_email,
            phone=company_phone,
            address=company_address,
            industry="Retail",
            company_type="Marketplace",
            language="English",
            country="Indonesia",
            province="PAPUA",
            city="KOTA JAYAPURA",
            district="HERAM",
            subdistrict="WAENA"
        )
        shot("filled company basic info")
        company_page.upload_company_document(
            document_type="Identification Card",
            file_path=str(file_path)
        )
        shot("uploaded company document")

        company_page.register_company(
            branch_name=fake.company_suffix()
        )
        shot("submitted company registration")


        company_page.verify_company_created(company_name)
    