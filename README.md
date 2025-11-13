⚙️ Installation
1️⃣ Clone Repository
git clone https://github.com/yourname/esuite-automation.git
cd esuite-automation

2️⃣ Create Virtual Environment
python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Setup Environment Variables
Isi sesuai kebutuhan:

BASE_URL=https://esuite.edot.id
ESUITE_EMAIL=it.qa@edot.id
ESUITE_PASSWORD=it.QA2025
HEADLESS=true

▶️ Running Tests
🔹 Run ALL tests
pytest --alluredir=reports/allure --headless true

🔹 Run only login test
pytest tests/test_login.py --alluredir=reports/allure

🔹 Run only company creation test
pytest tests/test_company.py --alluredir=reports/allure

🔹 Run with visible browser
pytest --headless false --alluredir=reports/allure

📊 Allure Report
Generate and open report:
allure serve reports/allure

Generate static site:
allure generate reports/allure -o reports/site --clean
