import sys, requests
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.common.by import By as BY
from selenium.webdriver.chrome.options import Options
from clear_screen import clear

uuids = open('replit_links.txt'.strip()).readlines()

def magnesium():
    try:

        clear()
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        webhook = input('Webhook: ')

        for link in uuids:
            link = link.strip()

            driver = webdriver.Chrome(options=chrome_options)
            
            try:
                driver.get(link)
            
            finally:
                WDW(driver, 10).until(EC.presence_of_all_elements_located)
                print(f'Loaded {link}')

            try:
                forks = driver.find_element(BY.XPATH, '/html/body/div[1]/div/main/div[2]/div/div/div[2]/div/button[2]')
                forks.click()
            
            finally:
                print(f'Loaded fork list')

            WDW(driver, 3).until(EC.presence_of_element_located((BY.XPATH, '/html/body/reach-portal/div[2]/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/span[1]')))

            amount_of_forks_element = driver.find_element(BY.XPATH, '/html/body/reach-portal/div[2]/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/span[1]')
            amount_of_forks_text = amount_of_forks_element.text
            amount_of_forks = int(amount_of_forks_text)

            if amount_of_forks > 50:
                load_element = driver.find_element(BY.XPATH, '/html/body/reach-portal/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/button')
                load_element.click()
        
            print(f'{amount_of_forks} forks found for {link}')

            webhook_payload = {"content": f"{amount_of_forks} forks found from ```{link}```", "embeds": [
        {
        "color": 7405312,
        "image": {"url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Repl.it_logo.svg/768px-Repl.it_logo.svg.png"}}]}

        requests.post(webhook, json=webhook_payload)

        driver.close()
        input(f'Finished, press enter to return to the main menu')
        magnesium()

    except KeyboardInterrupt:
        sys.exit()

if __name__ == '__main__':
    magnesium()
