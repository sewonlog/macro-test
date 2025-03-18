import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time

myId = os.getenv("TIKETLINK_ID")
myPw = os.getenv("TIKETLINK_PW")


# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

#화면 크기에 맞게 윈도우창 풀사이즈로 조절
driver.maximize_window()

page_url = 'https://www.ticketlink.co.kr/home/'

# 웹페이지가 로드될 때까지 2초를 대기
driver.implicitly_wait(time_to_wait=2)
driver.get(url=page_url)

# 스크롤 내리기
# driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)

# driver.implicitly_wait(time_to_wait=4)
time.sleep(2)

# 로그인
driver.find_element(By.XPATH, '//a[contains(@class, "header_util_link")]').click()

userId = driver.find_element(By.ID, "id")
userId.send_keys(myId)
userPwd = driver.find_element(By.ID, "pw")
userPwd.send_keys(myPw)
userPwd.send_keys(Keys.ENTER)