import sys
import requests
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.common.by import By as BY
from selenium.webdriver.chrome.options import Options
from concurrent.futures import ThreadPoolExecutor
from clear_screen import clear

uuids = open('replit_links.txt'.strip()).readlines()

def process_link(link):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    try:
        driver.get(link)
        WDW(driver, 10).until(EC.presence_of_all_elements_located)
        print(f'Loaded {link}')
        forks = driver.find_element(BY.XPATH, '/html/body/div[1]/div/main/div[2]/div/div/div[2]/div/button[2]')
        forks.click()
        print(f'Loaded fork list')
        WDW(driver, 3).until(EC.presence_of_element_located((BY.XPATH, '/html/body/reach-portal/div[2]/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/span[1]')))
        amount_of_forks_element = driver.find_element(BY.XPATH, '/html/body/reach-portal/div[2]/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/span[1]')
        amount_of_forks_text = amount_of_forks_element.text
        print(f'{link} has {amount_of_forks_text} forks')
    finally:
        driver.quit()

def magnesium():
    clear()
    webhook = input('Webhook: ')

    with ThreadPoolExecutor() as executor:
        for link in uuids:
            link = link.strip()
            executor.submit(process_link, link)
