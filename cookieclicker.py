import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = uc.Chrome()
driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie_id = "bigCookie"
cookies_id = "cookies"
product_price_prefix = "productPrice"
product_prefix = "product"

# Wait for language selection
WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'English')]"))
).click()

# Wait for the big cookie
WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.ID, cookie_id))
)

print("Game loaded. Starting automation...")

while True:
    try:
        # Click the cookie
        driver.find_element(By.ID, cookie_id).click()

        # Read cookie count
        cookies_text = driver.find_element(By.ID, cookies_id).text.split(" ")[0]
        cookies_count = int(cookies_text.replace(",", ""))

        # Loop through products (up to 4 for now)
        for i in range(4):
            price_element = driver.find_element(By.ID, f"{product_price_prefix}{i}")
            price_text = price_element.text.replace(",", "").strip()

            # Skip if price is not a digit (e.g., locked or blank)
            if not price_text.isdigit():
                continue

            price = int(price_text)

            # Buy if affordable
            if cookies_count >= price:
                product_element = driver.find_element(By.ID, f"{product_prefix}{i}")
                # Only click if it's not locked (has 'enabled' class)
                if "enabled" in product_element.get_attribute("class"):
                    product_element.click()
                    print(f"Bought Product {i} for {price}")
                    break

    except Exception as e:
        print("Retrying due to error:", e)
        time.sleep(0.5)
