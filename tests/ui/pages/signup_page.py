from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SignupPage:
    def __init__(self, driver):
        self.driver = driver 
        
    # Page 1
    def enter_name(self, name):
        self.driver.find_element(By.NAME, "name").send_keys(name)
        
    def enter_email(self, email):
        self.driver.find_element(By.CSS_SELECTOR, "input[data-qa='signup-email']").send_keys(email)
        
    def click_signup(self):
        button = self.driver.find_element(By.CSS_SELECTOR, "button[data-qa='signup-button']")
        self.driver.execute_script("arguments[0].click();", button)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        
    # Page 2
    def select_title(self, title):
        self.driver.find_element(By.CSS_SELECTOR, f"input[value='{title}']").click() # Mr / Mrs
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, f"input[value='{title}']"))
        ).click()
        
    def fill_account_info(self, password, day, month, year, first_name, last_name,
                           address, address2, country, state, city, zipcode, mobile):
        self.driver.find_element(By.ID, "password").send_keys(password)
        Select(self.driver.find_element(By.ID, "days")).select_by_value(day)
        Select(self.driver.find_element(By.ID, "months")).select_by_value(month)
        Select(self.driver.find_element(By.ID, "years")).select_by_value(year)
        self.driver.find_element(By.ID, "first_name").send_keys(first_name)
        self.driver.find_element(By.ID, "last_name").send_keys(last_name)
        self.driver.find_element(By.ID, "address1").send_keys(address)
        self.driver.find_element(By.ID, "address2").send_keys(address2)
        Select(self.driver.find_element(By.ID, "country")).select_by_value(country)
        self.driver.find_element(By.ID, "state").send_keys(state)
        self.driver.find_element(By.ID, "city").send_keys(city)
        self.driver.find_element(By.ID, "zipcode").send_keys(zipcode)
        self.driver.find_element(By.ID, "mobile_number").send_keys(mobile)

    def click_create_account(self):
        button = self.driver.find_element(By.CSS_SELECTOR, "button[data-qa='create-account']")
        self.driver.execute_script("arguments[0].click();", button)
    
    # Page 3
    def click_continue(self):
        button = self.driver.find_element(By.CSS_SELECTOR, "a[data-qa='continue-button']")
        self.driver.execute_script("arguments[0].click();", button)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Logged in as')]"))
        )
        #10초 동안 기다려, 이 조건이 될 때까지 ( 원하는 요소가 나타났는지 확인해( XPath 방식으로, 페이지에서 Logged in as라는 글자가 들어있는 요소) )
        
    def get_error_message(self):
        return self.driver.find_element(By.CSS_SELECTOR, "p[style*='color: red']").text
    
    def get_validation_message(self, data_qa_value):
        field = self.driver.find_element(By.CSS_SELECTOR, f"[data-qa='{data_qa_value}']")
        return self.driver.execute_script("return arguments[0].validationMessage;", field)