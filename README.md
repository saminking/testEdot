What This Project Does  
  
Framework ini digunakan untuk otomatisasi web eSuite, mencakup:  
  
✅ Login  
✅ Create Company  
✅ Verify Company List/Detail  
✅ Generate Allure Report (screenshots + steps)  
  
-- Installation  

1️. Clone Repository  
git clone https://github.com/yourname/esuite-automation.git  
cd esuite-automation  
  
2️. Create Virtual Environment  
python -m venv .venv  
source .venv/bin/activate    # Windows: .venv\Scripts\activate  
  
3️. Install Dependencies  
pip install -r requirements.txt  
  
4️. Setup Environment Variables  
Isi sesuai kebutuhan:  
  
BASE_URL=https://esuite.edot.id  
ESUITE_EMAIL=it.qa@edot.id  
ESUITE_PASSWORD=it.QA2025  
HEADLESS=true  
  
-- Running Tests  
1. Run ALL tests  
pytest --alluredir=reports/allure --headless true  
  
2. Run only login test  
pytest tests/test_login.py --alluredir=reports/allure  
  
3. Run only company creation test  
pytest tests/test_company.py --alluredir=reports/allure  
  
4. Run with visible browser  
pytest --headless false --alluredir=reports/allure  
  
-- Allure Report  
1. Generate and open report:  
allure serve reports/allure  
  
2. Generate static site:  
allure generate reports/allure -o reports/site --clean  
