from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Music:
    def __init__(self):
        chrome_options = Options()
        chrome_options.binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
        self.driver = webdriver.Chrome(options=chrome_options)

    def play(self, query):
        self.query = query
        self.driver.get("https://www.youtube.com")

        try:
            # Wait for the search input field
            search_input = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//input[@id="search"]'))
            )
            search_input.click()
            search_input.clear()
            search_input.send_keys(query)
            search_input.send_keys(Keys.RETURN)

            # Handle search suggestions if they appear
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, 'li.sbsb_c'))
                )
                first_suggestion = self.driver.find_element(By.CSS_SELECTOR, 'li.sbsb_c')
                first_suggestion.click()
            except:
                pass

            # Wait for the video link to be clickable
            video_link = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//a[@id="video-title"]'))
            )
            self.driver.execute_script("arguments[0].click();", video_link)

            # Wait for the video player to load
            video_player = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'html5-video-player'))
            )

            # Attempt to click the play button
            self.click_play_button()

            # Wait for the video to start playing
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'playing-mode'))
            )

            # Add a delay to keep the browser open for a while
            time.sleep(60)  # Keeps the browser open for 60 seconds after video starts playing
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            # Close the browser after a delay
            time.sleep(10)  # Wait for 10 seconds before closing the browser
            try:
                self.driver.quit()
            except:
                pass

    def click_play_button(self):
        try:
            # Attempt to click the play button
            play_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Play"]'))
            )
            self.driver.execute_script("arguments[0].click();", play_button)
        except Exception as e:
            print(f"Error clicking play button: {e}")
            # Retry clicking play button
            self.click_play_button()



