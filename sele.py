from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
import time

# Auto install and set ChromeDriver path
chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.get("https://www.google.com")

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)

imput_element = driver.find_element(By.CLASS_NAME, "gLFyf")   
imput_element.send_keys("Python" + Keys.ENTER)

link = driver.find_element(By.PARTIAL_LINK_TEXT, "Python")
link.click()

time.sleep(5)
driver.quit()
