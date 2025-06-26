"""
Task 2: Automated Testing with AI (Selenium)
Automates login page tests for valid and invalid credentials.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login(url, username, password, expected_in_title=None, expected_in_page=None):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(2)
    result = False
    if expected_in_title:
        result = expected_in_title in driver.title
    elif expected_in_page:
        result = expected_in_page in driver.page_source
    driver.quit()
    return result

if __name__ == "__main__":
    # Replace with actual login page URL and credentials
    url = "https://the-internet.herokuapp.com/login"
    print("Valid login:", test_login(url, "tomsmith", "SuperSecretPassword!", expected_in_page="You logged into a secure area!"))
    print("Invalid login:", test_login(url, "invalid_user", "wrong_pass", expected_in_page="Your username is invalid!")) 