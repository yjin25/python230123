# web2.py
#웹서버에 요청
import requests
#크롤링
from bs4 import BeautifulSoup

#주소
url = "https://www.daangn.com/fleamarket/"
response = requests.get(url)
#검색이 용이한 객체
soup = BeautifulSoup(response.text, "html.parser")

#검색
f = open("daangn.txt", "wt", encoding="utf-8")
posts = soup.find_all("div", attrs={"class":"card-desc"})
for post in posts:
    titleElem = post.find("h2", attrs={"class":"card-title"})
    priceElem = post.find("div", attrs={"class":"card-price"})
    addrElem = post.find("div", attrs={"class":"card-region-name"})
    title= titleElem.text.strip().replace("\n","")
    price= priceElem.text.strip().replace("\n","")
    addr= addrElem.text.strip().replace("\n","")
    print(f"{title}, {price}, {addr}")
    f.write(f"{title}, {price}, {addr}")

f.close()

    # <div class="card-desc">
    #   <h2 class="card-title">몽클레어 패딩 사이즈100</h2>
    #   <div class="card-price ">
    #     67,000원
    #   </div>
    #   <div class="card-region-name">
    #     부산 해운대구 우동
    #   </div>