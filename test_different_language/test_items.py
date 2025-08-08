from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def test_buttun_add(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    assert WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.ID, "add_to_basket_form"))), "Button 'add to basket' not found"
