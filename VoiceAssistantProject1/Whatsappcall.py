from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def make_whatsapp_call(contact_name):
    # Specify the path to the user data directory
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=C:/Path/To/Your/Chrome/User/Data")  # Change to your Chrome user data directory

    driver = webdriver.Chrome(options=options)  # Ensure the ChromeDriver path is set in your environment
    driver.get("https://web.whatsapp.com")

    # Wait for the WhatsApp Web interface to load
    try:
        print("Waiting for WhatsApp Web to load...")
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')))
        print("WhatsApp Web loaded.")
    except Exception as e:
        print(f"Exception occurred while waiting for WhatsApp Web to load: {e}")
        driver.save_screenshot("error_loading_whatsapp.png")
        driver.quit()
        return

    # Search for the contact name
    try:
        search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
        search_box.send_keys(contact_name)
        search_box.send_keys(Keys.ENTER)

        # Wait for the chat to open
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f'//span[@title="{contact_name}"]')))
        print(f"Chat opened for {contact_name}.")
    except Exception as e:
        print(f"Exception occurred while searching for contact: {e}")
        driver.save_screenshot("error_searching_contact.png")
        driver.quit()
        return

    # Locate and click the call button
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@title="Voice call"] | //div[@title="Call"]')))
        call_button = driver.find_element(By.XPATH, '//div[@title="Voice call"] | //div[@title="Call"]')
        call_button.click()
        print("Call button clicked.")
    except Exception as e:
        print(f"Exception occurred while locating call button: {e}")
        driver.save_screenshot("error_call_button.png")
    finally:
        time.sleep(5)  # Adjust the sleep time if needed
        driver.quit()
