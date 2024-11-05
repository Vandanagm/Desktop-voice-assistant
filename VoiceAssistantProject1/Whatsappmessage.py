from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

def send_whatsapp_message(contact_name, message):
    driver = webdriver.Chrome()
    driver.get("https://web.whatsapp.com")

    # Wait for the user to scan the QR code
    print("Please scan the QR code to log in.")
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
    )

    # Debug log
    print("QR code scanned, looking for search box.")

    # Search for the contact name and open chat
    try:
        search_box = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
        )
        search_box.send_keys(contact_name)
        search_box.send_keys(Keys.ENTER)
        print(f"Contact '{contact_name}' selected and chat opened.")
    except Exception as e:
        print(f"Failed to find the search box or contact: {e}")
        driver.quit()
        return

    # Wait for the chat to open
    try:
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="6"]'))
        )
        print("Chat box located.")
    except Exception as e:
        print(f"Failed to open chat: {e}")
        driver.quit()
        return

    # Send the message
    try:
        message_box = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="6"]'))
        )
        ActionChains(driver).move_to_element(message_box).click().send_keys(message).send_keys(Keys.ENTER).perform()
        print("Message sent successfully.")
    except Exception as e:
        print(f"Failed to send message: {e}")

    # Close the driver
    time.sleep(5)  # Allow time to see the result
    driver.quit()
