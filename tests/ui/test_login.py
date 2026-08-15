from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage



def test_login_success():
    driver = webdriver.Chrome()
    driver.get("https://automationexercise.com")
    driver.find_element(By.LINK_TEXT, "Signup / Login").click()
    
    login_page = LoginPage(driver) # login_page 연결
    
    # TC_LOGIN_001
    login_page.enter_email("qatest1234@example.com")
    login_page.enter_password("1234")
    login_page.click_login_button()
    
    assert "Logged in as" in driver.page_source # 현재 페이지 HTML에 Logged in as라는 글자가 반드시 있어야 한다. 없으면 Failed
    
    driver.quit()
    
def test_login_wrong_password():
    driver = webdriver.Chrome()
    driver.get("https://automationexercise.com")
    driver.find_element(By.LINK_TEXT, "Signup / Login").click()
    
    login_page = LoginPage(driver) # login_page 연결
    
    #TC_LOGIN_002
    login_page.enter_email("qatest1234@example.com")
    login_page.enter_password("4321")
    login_page.click_login_button()
    
    assert login_page.get_error_message() == "Your email or password is incorrect!"    
    # 오류 문구가 같은지 체크
    
    driver.quit()
    
def test_login_without_password():
    driver = webdriver.Chrome()
    driver.get("https://automationexercise.com")
    driver.find_element(By.LINK_TEXT, "Signup / Login").click()
    
    login_page = LoginPage(driver) # login_page 연결
    
    #TC_LOGIN_003
    login_page.enter_email("qatest1234@example.com")
    login_page.click_login_button()      
    
    assert login_page.get_validation_message("password")== "이 입력란을 작성하세요."  
    
    driver.quit()
    
def test_login_unregistered_email():
    driver = webdriver.Chrome()
    driver.get("https://automationexercise.com")
    driver.find_element(By.LINK_TEXT, "Signup / Login").click()
    
    login_page = LoginPage(driver) # login_page 연결
    
    #TC_LOGIN_004
    login_page.enter_email("testtest@example.com")
    login_page.enter_password("1234")
    login_page.click_login_button()
    
    assert login_page.get_error_message() == "Your email or password is incorrect!"

    driver.quit()
    
def test_login_invalid_email_format():
    driver = webdriver.Chrome()
    driver.get("https://automationexercise.com")
    driver.find_element(By.LINK_TEXT, "Signup / Login").click()

    login_page = LoginPage(driver) # login_page 연결

    #TC_LOGIN_005
    login_page.enter_email("qatest.com")
    login_page.enter_password("1234")
    login_page.click_login_button()

    assert login_page.get_validation_message("email") == "이메일 주소에 '@'를 포함해 주세요. 'qatest.com'에 '@'가 없습니다."

    driver.quit()
    
def test_login_without_email():
    driver = webdriver.Chrome()
    driver.get("https://automationexercise.com")
    driver.find_element(By.LINK_TEXT, "Signup / Login").click()
        
    login_page = LoginPage(driver) # login_page 연결
        
    #TC_LOGIN_006
    login_page.enter_password("1234")
    login_page.click_login_button()      
        
    assert login_page.get_validation_message("email") == "이 입력란을 작성하세요."  
        
    driver.quit()
    
def test_login_empty_credentials():
    driver = webdriver.Chrome()
    driver.get("https://automationexercise.com")
    driver.find_element(By.LINK_TEXT, "Signup / Login").click()

    login_page = LoginPage(driver) # login_page 연결

    #TC_LOGIN_007
    login_page.click_login_button()

    assert login_page.get_validation_message("email") == "이 입력란을 작성하세요."

    driver.quit()
