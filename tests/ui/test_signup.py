from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.signup_page import SignupPage

def test_signup_success():
    driver = webdriver.Chrome()
    driver.get("https://automationexercise.com")
    driver.find_element(By.LINK_TEXT, "Signup / Login").click()

    signup_page = SignupPage(driver)
    
    #TC_REGISTER_001
    # STEP 1
    signup_page.enter_name("Tester")
    signup_page.enter_email("qatest1234@example.com")
    signup_page.click_signup()
    # STEP 2
    signup_page.select_title("Mrs")
    signup_page.fill_account_info(
        password="1234", day="1", month="1", year="2000",
        first_name="QA", last_name="Tester",
        address="123 Test Street", address2="Apt 101",
        country="India", state="Test State", city="Test City",
        zipcode="12345", mobile="01012345678"
    )
    signup_page.click_create_account()
    # STEP 3
    signup_page.click_continue()

    assert "Logged in as" in driver.page_source

    driver.quit()
    
def test_signup_existing_email():
    driver = webdriver.Chrome()
    driver.get("https://automationexercise.com")
    driver.find_element(By.LINK_TEXT, "Signup / Login").click()

    signup_page = SignupPage(driver)
    #TC_SIGHUP_002
    signup_page.enter_name("Tester")
    signup_page.enter_email("qatest1234@example.com")  # 001에서 이미 가입된 이메일
    signup_page.click_signup()
    
    assert signup_page.get_error_message() == "Email Address already exist!"
    
    driver.quit()

def test_signup_invalid_format():
    driver = webdriver.Chrome()
    driver.get("https://automationexercise.com")
    driver.find_element(By.LINK_TEXT, "Signup / Login").click()

    signup_page = SignupPage(driver)

    #TC_REGISTER_003
    signup_page.enter_name("Tester")
    signup_page.enter_email("test1234.com")
    signup_page.click_signup()

    assert signup_page.get_validation_message("signup-email") == "이메일 주소에 '@'를 포함해 주세요. 'test1234.com'에 '@'가 없습니다."

    driver.quit()

def test_signup_all_required_fields_empty():
    driver = webdriver.Chrome()
    driver.get("https://automationexercise.com")
    driver.find_element(By.LINK_TEXT, "Signup / Login").click()

    signup_page = SignupPage(driver)

    #TC_REGISTER_004
    signup_page.enter_name("tesrer")
    signup_page.enter_email("qatest1111@example.com")
    signup_page.click_signup()
    signup_page.click_create_account()
    
    assert signup_page.get_validation_message("password") == "이 입력란을 작성하세요."
    
    driver.quit()