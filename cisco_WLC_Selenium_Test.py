# cisco_WLC_Selenium_Test.py

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import clipboard
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--allow-insecure-localhost")
chrome_options.add_argument("--ignore-urlfetcher-cert-requests")


driver = webdriver.Chrome(options=chrome_options)

# options=chrome_options

# driver = webdriver.Chrome()  # Chrome 드라이버를 사용하려면 Chrome 브라우저와 호환되는 버전의 드라이버가 필요합니다.

# WLC 로그인 페이지로 이동 ==> 페이지 이동 전 "연결이 비공개로 연결되어 있지 않습니다"로 넘어감
wlc_url = "https://192.168.40.130" 
driver.get(wlc_url)
time.sleep(10)