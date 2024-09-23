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

#화면 크기에 맞게 윈도우창 풀사이즈로 조절
driver.maximize_window()

page_url = 'https://tickets.interpark.com/'


# 웹페이지가 로드될 때까지 2초를 대기
driver.implicitly_wait(time_to_wait=2)
driver.get(url=page_url)

# 스크롤 내리기
# driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)

# 로그인
driver.find_element(By.XPATH,'//a[@title="로그인"]').click()

userId = driver.find_element(By.ID, 'userId')
userId.send_keys('id')
userPwd = driver.find_element(By.ID, "userPwd")
userPwd.send_keys('pw')
userPwd.send_keys(Keys.ENTER)


# 티켓 사이트 이동
driver.get('https://ticket.interpark.com/Contents/Sports/GoodsInfo?SportsCode=07001&TeamCode=PB004')
# 팝업창 닫기
#driver.find_element(By.XPATH,'//span[@class="blind"]').click()
#driver.find_element(By.CLASS_NAME, 'blind').click()
#driver.find_element(By.XPATH,'//*[@id="mainForm"]/div[9]/div/div[4]/a[4]').click()

# 스크롤 내리기
driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)

# 예매하기 버튼 클릭
driver.find_element(By.CLASS_NAME, 'BtnColor_Y').click()

# 새로운 탭으로 이동
print(driver.window_handles)
driver.switch_to.window(driver.window_handles[-1])

# 아이프레임으로 이동
driver.switch_to.frame(driver.find_element(By.XPATH, "//*[@id='ifrmSeat']"))

# 7초 기다림
time.sleep(9)

#팝업 닫기
driver.find_element(By.XPATH, "//a[@href=\"javascript:fnBookNoticeShowHide('');\"]").click()

#안심예매창 닫기
# driver.find_element(By.XPATH, "//a[@onclick='capchaHide()']").click()



