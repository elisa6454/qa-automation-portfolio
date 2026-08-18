from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.search_page import SearchPage

def test_search_success():
    driver = webdriver.Chrome()
    driver.get("https://automationexercise.com")
    products_link = driver.find_element(By.CSS_SELECTOR, "a[href='/products']")
    driver.execute_script("arguments[0].click();", products_link)

    search_page = SearchPage(driver)
    
    # TC_SEARCH_001
    search_page.search_product("Top")
    search_page.click_search_button()
    
    titles = search_page.get_result_titles()
    assert len(titles) > 0
    
    print(titles)
    
    driver.quit()
    
def test_search_partial():
    driver = webdriver.Chrome()
    driver.get("https://automationexercise.com")
    products_link = driver.find_element(By.CSS_SELECTOR, "a[href='/products']")
    driver.execute_script("arguments[0].click();", products_link)

    search_page = SearchPage(driver)
    
    # TC_SEARCH_002
    search_page.search_product("Dr")
    search_page.click_search_button()
    
    titles = search_page.get_result_titles()
    assert len(titles) > 0

    print(titles)
    
    driver.quit()
    
def test_search_insensitive():
    driver = webdriver.Chrome()
    driver.get("https://automationexercise.com")
    products_link = driver.find_element(By.CSS_SELECTOR, "a[href='/products']")
    driver.execute_script("arguments[0].click();", products_link)

    search_page = SearchPage(driver)
    
    # TC_SEARCH_003
    search_page.search_product("ToP")
    search_page.click_search_button()
    
    titles = search_page.get_result_titles()
    assert len(titles) > 0

    print(titles)
    
    driver.quit()
    
def test_search_special_characters():
    driver = webdriver.Chrome()
    driver.get("https://automationexercise.com")
    products_link = driver.find_element(By.CSS_SELECTOR, "a[href='/products']")
    driver.execute_script("arguments[0].click();", products_link)

    search_page = SearchPage(driver)
    
    # TC_SEARCH_004
    search_page.search_product("?!@#%")
    search_page.click_search_button()
    
    titles = search_page.get_result_titles()
    assert len(titles) == 0

    print(titles)
    
    driver.quit()

def test_search_leading_space():
    driver = webdriver.Chrome()
    driver.get("https://automationexercise.com")
    products_link = driver.find_element(By.CSS_SELECTOR, "a[href='/products']")
    driver.execute_script("arguments[0].click();", products_link)

    search_page = SearchPage(driver)
    
    # TC_SEARCH_005_1
    search_page.search_product(" Dress")
    search_page.click_search_button()
    
    titles = search_page.get_result_titles()
    assert len(titles) > 0

    print(titles)
    
    driver.quit()
    
def test_search_leading_spaces():
    driver = webdriver.Chrome()
    driver.get("https://automationexercise.com")
    products_link = driver.find_element(By.CSS_SELECTOR, "a[href='/products']")
    driver.execute_script("arguments[0].click();", products_link)

    search_page = SearchPage(driver)
    
    # TC_SEARCH_005_2
    search_page.search_product("  Dress")
    search_page.click_search_button()
    
    titles = search_page.get_result_titles()
    assert len(titles) == 0

    print(titles)
    
    driver.quit()
    
def test_search_trailing_spaces():
    driver = webdriver.Chrome()
    driver.get("https://automationexercise.com")
    products_link = driver.find_element(By.CSS_SELECTOR, "a[href='/products']")
    driver.execute_script("arguments[0].click();", products_link)

    search_page = SearchPage(driver)
    
    # TC_SEARCH_005_3
    search_page.search_product("Dress     ")
    search_page.click_search_button()
    
    titles = search_page.get_result_titles()
    assert len(titles) > 0

    print(titles)
    
    driver.quit()
    
def test_search_intermediate_spaces():
    driver = webdriver.Chrome()
    driver.get("https://automationexercise.com")
    products_link = driver.find_element(By.CSS_SELECTOR, "a[href='/products']")
    driver.execute_script("arguments[0].click();", products_link)

    search_page = SearchPage(driver)
    
    # TC_SEARCH_005_4
    search_page.search_product("Dr ess")
    search_page.click_search_button()
    
    titles = search_page.get_result_titles()
    assert len(titles) == 0

    print(titles)
    
    driver.quit()
        
def test_search_nonexist():
    driver = webdriver.Chrome()
    driver.get("https://automationexercise.com")
    products_link = driver.find_element(By.CSS_SELECTOR, "a[href='/products']")
    driver.execute_script("arguments[0].click();", products_link)

    search_page = SearchPage(driver)
    
    # TC_SEARCH_006
    search_page.search_product("leggings")
    search_page.click_search_button()
    
    titles = search_page.get_result_titles()
    assert len(titles) == 0

    print(titles)
    
    driver.quit()