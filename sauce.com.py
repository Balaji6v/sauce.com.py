from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


def login_and_scrape():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:

        driver.get("https://www.saucedemo.com/")
        wait = WebDriverWait(driver, 10)

        username = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
        password = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        login_button.click()


        time.sleep(2)

        title = driver.title
        current_url = driver.current_url

        print("Page Title:", title)
        print("Current URL:", current_url)

        with open("Webpage_task_11.txt", "w", encoding="utf-8") as f:
            f.write(driver.page_source)

        print("Webpage source saved to Webpage_task_11.txt")

    finally:
        driver.quit()

if __name__ == "__main__":
    login_and_scrape()
