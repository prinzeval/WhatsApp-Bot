# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# # Set up the WebDriver (example for Chrome)
# driver = webdriver.Chrome()

# # Open the target webpage
# driver.get('https://cc.animeheaven.me/video.mp4?a921a60c2aefde693e56c898a87792ab')

# # Wait for the page to load and potential ads to appear
# wait = WebDriverWait(driver, 10)
# wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
# time.sleep(10)

# # Optionally, remove or hide ads if you know their selectors
# try:
        
#     import pyautogui
#     import time
#     import subprocess

#     # Coordinates for the "Save as" option
#     save_as_x = 400
#     save_as_y = 711


#     # Wait for a few seconds to give you time to switch to the Chrome window

#     time.sleep(2)

#     # Perform a right-click at the desired location to open the context menu
#     pyautogui.rightClick(x=364, y=966)  # Adjust if necessary to right-click on the element you want to save

#     # Wait for the context menu to appear
#     time.sleep(1)

#     # Click on the "Save as" option
#     pyautogui.click(x=save_as_x, y=save_as_y)

#     # Optional: Wait to observe the action or handle file dialogs
#     time.sleep(5)
#     input("eneter")

#     # Optional: You might need additional code to handle file dialogs, depending on your OS
# finally:

# # Optionally, close the browser
#     driver.quit()





from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import concurrent.futures
import logging
import traceback
import time
chrome_driver_path = r'C:\Users\ELITEBOOK 1030\Desktop\chromedriver-win64\chromedriver.exe'

def scrape_data(link):
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run in headless mode
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')  # Disable GPU hardware acceleration
    chrome_options.add_argument('--log-level=3')  # Suppress logs

    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    data = []
    
    try:
        driver.get(link)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="film-detail-right"]')))
        
        sleep(random.randint(1, 4))  # Mimic human behavior

        jpg_list = []
        genres_list = []
        country_list = []
        director_list = []
        duration_list = []
        year_list = []
        actors_list = []
        descript_list = []

        details_cards = driver.find_elements(By.XPATH, '//div[@class="film-detail-right"]')

        for d_card in details_cards:
            elementHTML = d_card.get_attribute('outerHTML')
            elementsoup = BeautifulSoup(elementHTML, 'html5lib')
            details = elementsoup.find('div', class_='poster')

            if details:
                img_tag = details.find('img')
                if img_tag:
                    my_poster = img_tag.get('src')
                    jpg_list.append(my_poster)
            else:
                jpg_list.append('No Poster URL')
            
            tit = elementsoup.find('div', class_='about')
            if tit:
                h1_tag = tit.find('h1')
                if h1_tag:
                    my_title = h1_tag.text
                else:
                    my_title = 'No Title Found'
            else:
                my_title = 'No Title Found'

            genres = elementsoup.find('li', class_='label', string=lambda t: t.startswith('Genres:'))
            if genres:
                genres = genres.text.replace('Genres: ', '')
                genres_list.append(genres)
            else:
                genres_list.append('No Genres Found')

            country = elementsoup.find('li', class_='label', string=lambda t: t.startswith('Country:'))
            if country:
                country = country.text.replace('Country: ', '')
                country_list.append(country)
            else:
                country_list.append('No Country Found')

            director = elementsoup.find('li', class_='label', string=lambda t: t.startswith('Director:'))
            if director:
                director = director.text.replace('Director: ', '')
                director_list.append(director)
            else:
                director_list.append('No Director Found')

            duration = elementsoup.find('li', class_='label', string=lambda t: t.startswith('Duration:'))
            if duration:
                duration = duration.text.replace('Duration: ', '')
                duration_list.append(duration)
            else:
                duration_list.append('No Duration Found')

            year = elementsoup.find('li', class_='label', string=lambda t: t.startswith('Year:'))
            if year:
                year = year.text.replace('Year: ', '')
                year_list.append(year)
            else:
                year_list.append('No Year Found')

            actors = elementsoup.find('li', class_='label', string=lambda t: t.startswith('Actors:'))
            if actors:
                actors = actors.text.replace('Actors: ', '')
                actors_list.append(actors)
            else:
                actors_list.append('No Actors Found')

            descript = elementsoup.find('div', class_='textSpoiler', attrs={'data-height': '60'})
            if descript:
                descript = descript.text.strip()
                descript_list.append(descript)
            else:
                descript_list.append('No Description Found')

        data.append({
            'Poster URL': jpg_list[0] if jpg_list else 'No Poster URL',
            'Title': my_title,
            'Genres': genres_list[0] if genres_list else 'No Genres',
            'Country': country_list[0] if country_list else 'No Country',
            'Director': director_list[0] if director_list else 'No Director',
            'Duration': duration_list[0] if duration_list else 'No Duration',
            'Year': year_list[0] if year_list else 'No Year',
            'Actors': actors_list[0] if actors_list else 'No Actors',
            'Description': descript_list[0] if descript_list else 'No Description'
        })
    
    except Exception as e:
        logging.error(f"Error occurred while processing {link}: {e}")
        logging.debug(traceback.format_exc())  # Print stack trace for debugging
    
    finally:
        driver.quit()

    return data

# List of URLs to scrape
my_list = [
    # Add your URLs here
]

# Use ThreadPoolExecutor to run multiple instances concurrently
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(scrape_data, link) for link in my_list]
    results = [future.result() for future in concurrent.futures.as_completed(futures)]

# Flatten the results
flattened_results = [item for sublist in results for item in sublist]

# Convert to DataFrame and save to CSV
df = pd.DataFrame(flattened_results)
df.to_csv('out.csv', index=False)

print("Data has been successfully scraped and saved to 'out.csv'.")
