from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
from typing import List
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
import time
import config as cf
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Chrome options and service
options = webdriver.ChromeOptions()
options.add_argument(f"user-data-dir={cf.local['userDataDir']}")
service = Service(cf.local["executablePath"])

# Initialize the browser
driver = webdriver.Chrome(service=service, options=options)

# Blacklist of contacts
BLACKLIST = {"OC Community 8", "Müĝïŵ@r@", "ScholarshipsAds 4", "ScholarshipsAds 2", "Anime Updates", "Nation", "Nigeria Association of Lefke Students, TRNC."}

def navigate_to_whatsapp():
    if "web.whatsapp.com" not in driver.current_url:
        logger.info("Navigating to WhatsApp Web...")
        driver.get("https://web.whatsapp.com/")
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="side"]'))
        )
        time.sleep(10)  # Wait for WhatsApp to load

def get_unread_messages() -> List[str]:
    contact_names = set()  # Use a set to avoid duplicates
    try:
        logger.info("Getting unread messages...")
        navigate_to_whatsapp()

        # Get the page source
        html = driver.page_source
        
        # Parse the page source
        soup = BeautifulSoup(html, 'html.parser')
        div_elements = soup.find_all('div', class_='x10l6tqk xh8yej3 x1g42fcv')
        for div in div_elements:
            spans = div.find_all('span')

            for span in spans:
                if 'unread message' in span.get('aria-label', '').lower():
                    contact_name_span = div.find('span', dir="auto", style="min-height: 0px;")
                    if contact_name_span:
                        contact_name = contact_name_span.text
                        contact_names.add(contact_name)  # Add to set

        logger.info(f"Contacts extracted: {list(contact_names)}")

    except Exception as e:
        logger.error(f"An error occurred while getting unread messages: {e}")

    return list(contact_names)  # Convert set back to list

def send_whatsapp_message(recipient_name: str, message_text: str):
    try:
        if recipient_name in BLACKLIST:
            logger.info(f"Skipping blacklisted contact: {recipient_name}")
            return

        logger.info(f"Sending message to {recipient_name}...")
        # Search for the contact
        search_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div'))
        )
        
        # Use ActionChains to interact with the search field
        actions = ActionChains(driver)
        actions.move_to_element(search_field).click().send_keys(recipient_name).send_keys(Keys.RETURN).perform()
        
        try:
            # Wait for the message input field to be present
            message_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'))
            )
            
            # Send the message using ActionChains
            actions.move_to_element(message_field).click().send_keys(message_text).send_keys(Keys.RETURN).perform()
            
            logger.info(f"Message sent to {recipient_name}: {message_text}")

            # Close the chat box
            try:
                # Wait for the close chat button to be clickable
                close_chat_icon = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/header/div[3]/div/div[3]/div/div/span'))
                )
                close_chat_icon.click()
                
                close_chat_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/span[5]/div/ul/div/div/li[3]'))
                )
                close_chat_button.click()

            except TimeoutException:
                logger.warning("Failed to close chat box. Elements not clickable.")

        except TimeoutException:
            logger.warning(f"Message input field not found for {recipient_name}. Clearing search input and skipping this contact.")
            # Clear the search input
            search_field.clear()

    except StaleElementReferenceException:
        logger.warning("Stale element reference. Refetching elements...")
        # Retry sending the message
        send_whatsapp_message(recipient_name, message_text)

    except Exception as e:
        logger.error(f"An error occurred while sending message to {recipient_name}: {e}")

def send_messages_to_contacts(contact_names: List[str], message_text: str):
    for contact in contact_names:
        send_whatsapp_message(contact, message_text)

def close_browser():
    driver.quit()
