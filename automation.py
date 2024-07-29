from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import config as cf
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

from typing import List

def bring_contact_data(contact_data: List[str]):
    for contact in contact_data:
        print("Contact extracted:", contact)




# def send_whatsapp_message(recipient_name: str, message_text: str):
 
#     # Initialize Chrome options
#     options = webdriver.ChromeOptions()
#     # Add the user-data-dir argument to use a specific Chrome profile
#     options.add_argument(f"user-data-dir={cf.local['userDataDir']}")

#     # Initialize Chrome service
#     service = Service(cf.local["executablePath"])

#     # Initialize Chrome WebDriver with the specified service and options
#     driver = webdriver.Chrome(service=service, options=options)

#     try:
#         # Navigate to WhatsApp Web
#         driver.get("https://web.whatsapp.com/")
        
#         # Wait for the search field to be present
#         search_field = WebDriverWait(driver, 60).until(
#             EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div'))
#         )
        
#         # Use ActionChains to interact with the search field
#         actions = ActionChains(driver)
#         actions.move_to_element(search_field).click().send_keys(recipient_name).send_keys(Keys.RETURN).perform()
        
#         # Allow time for the chat to open
#         time.sleep(5)
        
#         # Wait for the message input field to be present
#         message_field = WebDriverWait(driver, 60).until(
#             EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'))
#         )
        
#         # Send the message using ActionChains
#         actions = ActionChains(driver)
#         actions.move_to_element(message_field).click().send_keys(message_text).send_keys(Keys.RETURN).perform()
        
#         print(f"Message sent to {recipient_name}: {message_text}")

#         time.sleep(10)
#         input("go")

#     finally:
#         # Close the browser and end the session
#         driver.quit()
