import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Sample names
names = ["Raj", "Simran", "Arjun", "Pooja"]

# Initialize the WebDriver
driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
time.sleep(2)  # Wait for the page to load

for i in range(3):
    print(f"\n--- Filling Form {i+1} ---")
    
    first = random.choice(names)
    last = random.choice(names)
    
    # Locate form fields
    first_name_field = driver.find_element(By.NAME, "my-text")
    last_name_field = driver.find_element(By.NAME, "my-password")
    
    # Clear and fill the fields
    first_name_field.clear()
    last_name_field.clear()
    first_name_field.send_keys(first)
    last_name_field.send_keys(last)
    
    # Submit the form
    submit_button = driver.find_element(By.TAG_NAME, "button")
    submit_button.click()
    
    time.sleep(2)  # Wait for the form to submit
    driver.back()  # Navigate back to the form page
    time.sleep(2)  # Wait for the page to load

driver.quit()
