

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
