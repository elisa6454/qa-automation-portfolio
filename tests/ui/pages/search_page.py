from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage:
    def __init__(self, driver):
        self.driver = driver
    
    def search_product(self, keyword):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "search_product"))
            )
        self.driver.find_element(By.ID, "search_product").send_keys(keyword)
    
    def click_search_button(self):
        button = self.driver.find_element(By.ID, "submit_search")
        self.driver.execute_script("arguments[0].click();", button)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "features_items"))
        )
    
    def get_result_titles(self):
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".productinfo p")
        return [e.text for e in elements]