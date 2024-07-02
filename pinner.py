import urllib.request
import urllib.response
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
import datetime
import time
import csv
import requests
import shutil

profile_path = "C:\\Users\\Syed Aalehuzoor\\AppData\\Local\\Google\\Chrome\\User Data"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"user-data-dir={profile_path}")
chrome_options.add_argument('--profile-directory=Default') #e.g. Profile 3

driver = WebDriver(options=chrome_options)

pinned_urls = []
with open('pinned.csv', 'r', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        pinned_urls.append(row[0])

urls = []
with open('scraped.csv', 'r', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] not in pinned_urls:
            urls.append(row[0])

for url in urls:
    driver.get(url=url)
    image = driver.find_element(By.XPATH, '//*[@id="landingImage"]').screenshot_as_png
    #with open(file='image.png', mode='wb') as file:
        #file.write(image)
    title_element = driver.find_element(By.XPATH, '//*[@id="title"]')
    title = title_element.text
    description_element = driver.find_element(By.XPATH, '//*[@id="productOverview_feature_div"]/div[1]/table/tbody')
    description = description_element.text
    print(title)
    print(description)
    text = driver.find_element(By.XPATH, '//*[@id="amzn-ss-text-link"]/span/strong/a')
    text.click()
    time.sleep(3)
    full = driver.find_element(By.XPATH, '//*[@id="amzn-ss-full-link-radio-button"]/label/i')
    full.click()
    time.sleep(3)
    textarea = driver.find_element(By.XPATH, '//*[@id="amzn-ss-text-fulllink-textarea"]')
    ref_link = textarea.get_attribute('value')

    print(ref_link)
    

driver.quit()
