import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service('C:/Users/seong/chromedriver.exe')
service.start()

driver = webdriver.Remote(service.service_url)

login_url = "https://ticket.interpark.com/Gate/TPLogin.asp"
driver.get(login_url)

time.sleep(3)
driver.quit()
