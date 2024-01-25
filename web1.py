# web1. py
#웹 크롤링
from bs4 import BeautifulSoup

#페이지를 로딩
page = open(r"C:\\work\\test01.html", "rt", encoding="utf-8").read()

#검색이 용이한 객체
soup = BeautifulSoup(page, "html.parser")

#전체 문서 보기
# print(soup.prettify())

#<p> 전체를 검색
# print(soup.find_all("p"))

#<p> 하나만 검색
# print(soup.find("p"))

#<p class='outer-text'> 조건
# print(soup.find_all("p", class_="outer-text"))

#최근 스타일: attrs 속성(Atrributes)
#print(soup.find_all("p", attrs={"class":"outer-text"}))

#태그 안쪽에 컨텐츠만 가져오기: .text
for tag in soup.find_all("p"):
    title = tag.text.strip()
    print(title)