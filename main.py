import time
import config
import webbrowser
import undetected_chromedriver.v2 as uc

from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver



chrome_options = uc.ChromeOptions()

for opt in config.chrome_options:
    chrome_options.add_argument(opt)



driver: webdriver.Chrome = uc.Chrome(options=chrome_options)
driver.delete_all_cookies()
driver.get(config.AUTH_URL)


driver.find_element("id", "identifierId").send_keys(config.LOGIN)
driver.find_element("id", "identifierNext").click()

loaded = False

while not loaded:
    try:
        driver.find_element("xpath", '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(config.PASSWORD)
        loaded = True
    except NoSuchElementException:
        time.sleep(1)

driver.find_element("xpath", '//*[@id="passwordNext"]/div/button').click()

time.sleep(5)
driver.get("https://mail.google.com/mail/u/0/#inbox")

time.sleep(20)
