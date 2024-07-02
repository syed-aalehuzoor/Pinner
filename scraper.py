from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv
import re

profile_path = "C:\\Users\\Syed Aalehuzoor\\AppData\\Local\\Google\\Chrome\\User Data"

chrome_options = Options()
chrome_options.add_argument(f"user-data-dir={profile_path}")
chrome_options.add_argument('--profile-directory=Default') # e.g. Profile 3

driver = WebDriver(options=chrome_options)

# Function to check if URL already exists in CSV
def url_not_in_csv(url, csv_file):
    with open(csv_file, 'r', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if url in row:
                return False
    return True

csv_file = 'scraped.csv'

amazon_product_pattern = re.compile(r'https://www.amazon.com/[a-zA-Z0-9-]+/dp/[a-zA-Z0-9]+')

# Track unique URLs and pages visited
unique_urls = set()
urls_found = 0
page = 1
# Base URL to start crawling
base_url = "https://www.amazon.com/s?i=garden&rh=n%3A18351213011&fs=true&qid=1719903414&ref=sr_pg_1"


while urls_found < 100:

    driver.get(base_url)
    time.sleep(5)  # Adjust this delay as needed

    # Scroll to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
    time.sleep(5)  # Adjust this delay as needed for the page to fully load after scrolling

    # Find all links on the page
    elements = driver.find_elements(By.TAG_NAME, 'a')

    for element in elements:
        href = element.get_attribute('href')
        if href and re.match(amazon_product_pattern, href):
            if href not in unique_urls and url_not_in_csv(href, csv_file):
                unique_urls.add(href)
                urls_found += 1
                print(urls_found)
                if urls_found >= 100:
                    break
    page += 1
    base_url = f'https://www.amazon.com/s?i=garden&rh=n%3A18351213011&fs=true&qid=1719903414&ref=sr_pg_{page}'

# Write unique URLs to CSV
with open(csv_file, 'a', newline='') as f:
    writer = csv.writer(f)
    for item in unique_urls:
        writer.writerow([item])

driver.quit()