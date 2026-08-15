from selenium.webdriver.common.by import By

class LoginPage:
    
    def __init__(self, driver):
        self.driver = driver 
    # 브라우저를 받아서 보관 - ex) chrome 
    
    def enter_email(self, email):
        self.driver.find_element(By.NAME, "email").send_keys(email)
    # chrome.웹페이지 요소 찾아(NAME이라는 속성을 기준으로, email인 요소를 찾아라)[찾았다!].찾은 입력창에 email 값을 입력해.
    
    def enter_password(self, password):
        self.driver.find_element(By.NAME, "password").send_keys(password)
        
    def click_login_button(self):
        button = self.driver.find_element(By.CSS_SELECTOR, "button[data-qa='login-button']")
        self.driver.execute_script("arguments[0].click();", button)
    # 광고 iframe이 로그인 버튼을 가려, 일반 click()이 차단되어서 있어 JS click 사용
        
    def get_error_message(self):
        return self.driver.find_element(By.CSS_SELECTOR, "p[style*='color: red']").text
    # 아이디/비번 다 입력했는데 틀렸을 때: "Your email or password is incorrect!" 
    
    def get_validation_message(self, field_name):
        field = self.driver.find_element(By.NAME, field_name)
        return self.driver.execute_script("return arguments[0].validationMessage;", field)
    # JS를 실행해서 (입력창의 validationMessage(브라우저가 띄운 검증 메시지)를 가져와, field(예: email 또는 password 입력창) )
    
    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT, "Logout").click()