from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver (example for Chrome)
driver = webdriver.Chrome()

# Open the target webpage
driver.get('https://eplayvid.net/watch/db52135d2d86b25')

# Wait for the page to load and potential ads to appear
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

# Optionally, remove or hide ads if you know their selectors
try:
    ad_selectors = [
        'div.ad-container',  # Replace with actual ad selectors
        'iframe.ad-frame'
    ]
    for selector in ad_selectors:
        ads = driver.find_elements(By.CSS_SELECTOR, selector)
        for ad in ads:
            driver.execute_script("arguments[0].style.display = 'none';", ad)
except Exception as e:
    print(f"Error handling ads: {e}")

# Function to calculate and click the center of the screen
def click_center(driver):
    # Calculate the center of the viewport
    viewport_width = driver.execute_script("return window.innerWidth;")
    viewport_height = driver.execute_script("return window.innerHeight;")
    center_x = viewport_width / 2
    center_y = viewport_height / 2

    # Use ActionChains to move to the center and click
    actions = ActionChains(driver)
    actions.move_by_offset(center_x, center_y).click().perform()

    # Reset the offset (important to avoid cumulative offsets)
    actions.move_by_offset(-center_x, -center_y).perform()

# Click in the center 9 times with a 2-second interval
for _ in range(12):
    click_center(driver)
    print("Click performed at the center of the screen.")
    time.sleep(2)  # Wait for 2 seconds between clicks

# Wait for the specific element to be clickable and then click it
import pyautogui
import time
import subprocess

    # Coordinates for the "Save as" option
save_as_x = 400
save_as_y = 711


    # Wait for a few seconds to give you time to switch to the Chrome window

time.sleep(2)

    # Perform a right-click at the desired location to open the context menu
pyautogui.rightClick(x=364, y=966)  # Adjust if necessary to right-click on the element you want to save

    # Wait for the context menu to appear
time.sleep(1)

    # Click on the "Save as" option
pyautogui.click(x=save_as_x, y=save_as_y)

    # Optional: Wait to observe the action or handle file dialogs
time.sleep(5)
input("eneter")

# Optional: You might need additional code to handle file dialogs, depending on your OS


# Optionally, close the browser
driver.quit()










    # # Calculate center of the viewport
    # body = driver.find_element(By.TAG_NAME, 'body')
    # width = body.size['width']
    # height = body.size['height']
    # center_x = width / 2
    # center_y = height / 2

    # # Function to click at the center of the screen
    # def click_center(x, y):
    #     actions = ActionChains(driver)
    #     actions.move_by_offset(x, y).click().perform()
    
    # # Perform 8 clicks at the center with a 2-second interval
    # for i in range(8):
    #     click_center(center_x, center_y)
    #     print(f'Click {i + 1} at center ({center_x}, {center_y})')
    #     time.sleep(2) 







# # Define message templates
# TEMPLATES = {
#     "welcome": "Hello! Welcome to our service. What do you want to order? Reply 'yes' to continue or 'no' to exit.",
#     "order_menu": (
#         "Here's our menu:\n"
#         "1. Apple - $1.99 per lb\n"
#         "2. Banana - $0.99 each\n"
#         "3. Carrot - $1.49 per lb\n"
#         "4. Chicken Breast - $6.99 per lb\n"
#         "5. Coffee - $2.99 per lb\n"
#         "6. Donut - $1.99 each\n"
#         "7. Egg - $1.99 per 6\n"
#         "8. Flour - $2.99 per lb\n"
#         "9. Grain Bread - $2.99 per loaf\n"
#         "10. Hamburger - $3.99 per lb\n"
#         "Reply with the number of the item you want to order or 'done' to finish."
#     ),
#     "thank_you": "Thank you for your message. A human will get back to you soon."
# }

# # Define responses for menu selection
# FOOD_ITEMS = {
#     "1": "Apple",
#     "2": "Banana",
#     "3": "Carrot",
#     "4": "Chicken Breast",
#     "5": "Coffee",
#     "6": "Donut",
#     "7": "Egg",
#     "8": "Flour",
#     "9": "Grain Bread",
#     "10": "Hamburger"
# }

# def handle_user_interaction(driver, recipient_name: str, user_message: str):
#     message_text = user_message.lower()
    
#     if message_text == 'hello':
#         send_whatsapp_message(driver, recipient_name, TEMPLATES["welcome"])
#     elif message_text == 'yes':
#         send_whatsapp_message(driver, recipient_name, TEMPLATES["order_menu"])
#     elif message_text == 'no':
#         send_whatsapp_message(driver, recipient_name, TEMPLATES["thank_you"])
#     elif message_text in FOOD_ITEMS:
#         item = FOOD_ITEMS[message_text]
#         send_whatsapp_message(driver, recipient_name, f"You have selected {item}.")
#         send_whatsapp_message(driver, recipient_name, TEMPLATES["thank_you"])
#     elif message_text == 'done':
#         send_whatsapp_message(driver, recipient_name, TEMPLATES["thank_you"])
#     else:
#         send_whatsapp_message(driver, recipient_name, "Sorry, I didn't understand your response.")

# def send_messages_to_contacts(contact_names: List[str], user_message: str):
#     driver = get_driver()
#     navigate_to_whatsapp(driver)
#     for contact in contact_names:
#         handle_user_interaction(driver, contact, user_message)
#     driver.quit()
