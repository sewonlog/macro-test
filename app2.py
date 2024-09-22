from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time



# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
#driver.set_window_size(1900, 1000)
#driver.manage().window().maximize()
yse24_rul = 'https://tickets.interpark.com/'


# 웹페이지가 로드될 때까지 2초를 대기
driver.implicitly_wait(time_to_wait=2)
driver.get(url=yse24_rul)

# 스크롤 내리기
# driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)

# 로그인
driver.find_element(By.XPATH,'//a[@title="로그인"]').click()

userId = driver.find_element(By.ID, 'userId')
userId.send_keys('아이디')
userPwd = driver.find_element(By.ID, "userPwd")
userPwd.send_keys('비번')
userPwd.send_keys(Keys.ENTER)


# 티켓 사이트 이동
driver.get('https://ticket.interpark.com/Contents/Sports/GoodsInfo?SportsCode=07001&TeamCode=PB004')
# 팝업창 닫기
#driver.find_element(By.XPATH,'//span[@class="blind"]').click()
#driver.find_element(By.CLASS_NAME, 'blind').click()
#driver.find_element(By.XPATH,'//*[@id="mainForm"]/div[9]/div/div[4]/a[4]').click()

# 예매하기 버튼 클릭
driver.find_element(By.XPATH, "//a[@onclick=\"CallWynsBooking('True','Y','Y','N','24012119','','20240923','001','','','111087390','abfe07d785ee8ac465ad9b64ce3f6b77','1727057496048','N','N')\"]")