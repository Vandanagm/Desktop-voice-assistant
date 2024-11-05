from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class infow:
    def __init__(self):
        chrome_options = Options()
        chrome_options.binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
        self.driver = webdriver.Chrome(options=chrome_options)

    def get_info(self, query):
        self.query = query
        try:
            self.driver.get("https://www.wikipedia.org")

            # Wait for the search input field to be clickable
            search = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="searchInput"]'))
            )
            search.click()
            search.clear()
            search.send_keys(query)
            search.send_keys(Keys.RETURN)

            # Add a delay to keep the browser open after performing actions
            time.sleep(10)  # Keep the browser open for 10 seconds after performing actions

        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            # Close the browser after a delay
            time.sleep(5)  # Wait for 5 seconds before closing the browser
            try:
                self.driver.quit()
            except:
                pass


