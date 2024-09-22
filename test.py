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
driver.set_window_size(1900, 1000)
yse24_rul = 'http://ticket.yes24.com/'


# 웹페이지가 로드될 때까지 2초를 대기
driver.implicitly_wait(time_to_wait=2)
driver.get(url=yse24_rul)

# 스크롤 내리기
driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)

# 로그인
driver.find_element(By.XPATH,'//*[@id="consiceLogin"]').click()

userId = driver.find_element(By.ID, 'SMemberID')
userId.send_keys('아이디')
userPwd = driver.find_element(By.ID, "SMemberPassword")
userPwd.send_keys('비밀번호')
userPwd.send_keys(Keys.ENTER)


# 티켓 사이트 이동
driver.get('http://ticket.yes24.com/Special/49580')
driver.find_element(By.XPATH,'//*[@id="mainForm"]/div[9]/div/div[4]/a[4]').click()




#예매하기 탭 이동
time.sleep(1)
print('--------------------')
print(driver.window_handles)
driver.switch_to.window(driver.window_handles[-1])

# 날짜 선택
driver.find_element(By.CLASS_NAME,'select').click()
driver.find_element(By.XPATH,'//*[@id="btnSeatSelect"]').click()

# 구역, 좌석 선택하기
driver.switch_to.frame(driver.find_element(By.XPATH,'//*[@id="divFlash"]/iframe'))

driver.find_element(By.XPATH,'//*[@id="area5"]').click()
#driver.find_element(By.XPATH,'//*[@id="t5700156"]').click()
driver.find_element(By.XPATH,'//*[@id="divSeatArray"]/div[string-length(@title)>0]').click()
#driver.find_element(By.XPATH,'//*[@id="divSeatArray"]/div[120]').click()
#driver.find_element((By.XPATH("//*[@attribute='grade']"))).click()


# 좌석선택 완료
driver.find_element(By.XPATH,'//*[@id="form1"]/div[3]/div[2]/div/div[2]/p[2]/a/img').click()


# 할인/쿠폰
driver.switch_to.default_content()
driver.find_element(By.XPATH,'//*[@id="StepCtrlBtn03"]/a[2]/img').click()

# 수령방법
time.sleep(3)  ## 주문자 정보 받아오기``
driver.find_element(By.XPATH,'//*[@id="StepCtrlBtn04"]/a[2]/img').click()

#결제방법
driver.find_element(By.XPATH,'//*[@id="rdoPays22"]').click()  #무통장 입금

select = Select(driver.find_element(By.XPATH,'//*[@id="selBank"]'))
select.select_by_index(1)

# 예매하기
driver.find_element(By.XPATH,'//*[@id="cbxAllAgree"]').click()
driver.find_element(By.XPATH,'//*[@id="imgPayEnd"]').click()