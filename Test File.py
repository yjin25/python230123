# Test File.py

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import clipboard
from selenium.webdriver.common.by import By

# Chrome 옵션 설정

# 웹 드라이버 초기화
chrome_options = Options()

# WLC 로그인 페이지로 이동 ==> 페이지 이동 전 "연결이 비공개로 연결되어 있지 않습니다"로 넘어감
# SSL 인증서 무시

chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--allow-insecure-localhost")
chrome_options.add_argument("--ignore-urlfetcher-cert-requests")
# chrome_options.add_argument("--headless")

# Chrome 드라이버를 사용하려면 Chrome 브라우저와 호환되는 버전의 드라이버가 필요합니다.
driver = webdriver.Chrome(options=chrome_options)  


# WLC 로그인 페이지로 이동 ==> 페이지 이동 전 "연결이 비공개로 연결되어 있지 않습니다"로 넘어감
wlc_url = "https://192.168.40.241" 
driver.get(wlc_url)
time.sleep(3)


#로그인 창에 아이디/비밀번호 입력
username = "admin"
clipboard.copy(username)
#mac은 COMMAND, window는 CONTROL
driver.find_element(By.XPATH,'//*[@id="username"]').send_keys(Keys.CONTROL, 'v')

password = "admin"
clipboard.copy(password)
driver.find_element(By.XPATH,'//*[@id="password"]').send_keys(Keys.CONTROL, 'v')
time.sleep(1)

# # 로그인 버튼 클릭
driver.find_element(By.XPATH,'//*[@id="login"]').click()  # 실제 웹 페이지의 버튼 선택자에 따라 변경

# 로그인 후 작업 수행 (이 부분을 원하는 작업으로 변경 가능)
time.sleep(5)  # 로그인 완료 후 페이지 로딩을 기다리기 위한 간격

# # 작업 완료 후 브라우저 종료
# driver.quit()

while True:
    pass


# ========================================================
# 여기까지 자동로그인

# 로그인 세션 남아있음 => 웹 크롤링으로 점검서에 있는 데이터 받아오기, GUI로 구현?
