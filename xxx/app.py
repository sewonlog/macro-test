import time
from selenium import webdriver #동적 사이트 수집
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver as wb

# wb.Chrome()


# 크롬드라이버 경로 설정
service = Service('C:/Users/sewon/chromedriver-win64/chromedriver.exe')
service.start()

# 드라이버 설정 (Remote가 아닌 Chrome을 사용)
driver = webdriver.Chrome(service=service)

# 로그인 페이지로 이동
login_url = "https://tickets.interpark.com/"
driver.get(login_url)

# 페이지 로드 대기
# time.sleep(7)

# 브라우저 종료
# driver.quit()
