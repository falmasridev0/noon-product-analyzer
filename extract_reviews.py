from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from chromedriver_py import binary_path

import tempfile

def extract_reviews(url):
    options = webdriver.ChromeOptions()
    temp_user_data_dir = tempfile.mkdtemp()
    options.add_argument(f"--user-data-dir={temp_user_data_dir}")
    # options.add_argument("--headless")              
    # options.add_argument("--no-sandbox")                 
    options.add_argument("--disable-dev-shm-usage")  
    # options.add_argument('--no-first-run')
    # options.add_argument('--no-service-autorun')
    # options.add_argument('--no-default-browser-check')


    driver = webdriver.Chrome(service=webdriver.ChromeService(executable_path=binary_path),options=options)
    driver.get(url)
    
    reviews = []





    while True:
            time.sleep(1)
            #set page load timeout to 10 seconds
            driver.set_page_load_timeout(5)
            html =  BeautifulSoup(driver.page_source, "html.parser")
            result = html.find_all("div",{"class":"CollapsibleText_textContainer__jUZvK"})


            result = pd.Series(result).apply(lambda row : row.text)
            reviews.extend(result)
            try:
                next_button = driver.find_element(By.CSS_SELECTOR, 'li.next a[aria-label="Next page"]')

                is_disabled = next_button.get_attribute("aria-disabled") == "true"
                if  is_disabled and len(result) <= 15:
                    break          
                else:
                    driver.execute_script("arguments[0].click();", next_button)   
            except NoSuchElementException:
                 print("all data retrived.")
                 break
                 


 

    print(len(reviews))

    driver.quit()
    return reviews


