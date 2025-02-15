import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920x1080')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-insecure-localhost')

driver = webdriver.Chrome(options=options)

driver.get('https://kenkoooo.com/atcoder/#/table')



try:
    time.sleep(5)
    table = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[3]/div/div[1]/div[2]/table/tbody')
    for row in table.find_elements(By.TAG_NAME, 'tr'):
        idx = 0
        for cell in row.find_elements(By.TAG_NAME, 'td'):
            try:
                if idx == 0:
                    print(cell.text)
                else:
                    diff = cell.find_element(By.CLASS_NAME, 'table-problem-point').text
                    color = cell.find_element(By.TAG_NAME, 'a').get_attribute('class')
                    color = color.split('difficulty-')[1]
                    print(diff, color)

            except Exception as e:
                pass
            idx += 1
            
except Exception as e:
    print(e)

driver.quit()