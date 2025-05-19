import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Auto install correct ChromeDriver
chromedriver_autoinstaller.install()

# Chrome options for stability on Mac
options = Options()
# options.add_argument("--headless=new")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)
driver.set_page_load_timeout(60)  # Increase timeout

driver.get("https://www.techlistic.com/p/selenium-practice-form.html")

time.sleep(2)
driver.find_element(By.NAME, "firstname").send_keys("Mayank")
driver.find_element(By.NAME, "lastname").send_keys("Kumar")
driver.find_element(By.ID, "sex-0").click()
driver.find_element(By.ID, "exp-2").click()
driver.find_element(By.ID, "datepicker").send_keys("15-05-2025")

# Use JS to click checkboxes
driver.execute_script("arguments[0].click();", driver.find_element(By.ID, "profession-1"))
driver.execute_script("arguments[0].click();", driver.find_element(By.ID, "tool-2"))

# Wait & submit
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "submit"))).click()

print("✅ Form submitted successfully!")
time.sleep(2)
driver.quit()
