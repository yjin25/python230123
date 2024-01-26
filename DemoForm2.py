# DemoForm2.py(로직 코딩) + DemoForm2.ui(화면을 XML문서 저장)
import sys 
import requests
#Qt패키지를 임포트 
from PyQt5.QtWidgets import *
from PyQt5 import uic 
#웹사이트에 페이지 실행을 요청
import urllib.request
#크롤링
from bs4 import BeautifulSoup

#디자인 문서를 로딩
form_class = uic.loadUiType("c:\\work\\DemoForm2.ui")[0]

#윈도우 클래스 정의(QMainWindows로 변경 : 기능이 더 많음)
class DemoForm(QMainWindow, form_class):
    #초기화 메서드
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def firstClick(self):

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
        self.label.setText("첫번째 버튼")
    def secondClick(self):
        self.label.setText("두번째 화면")
    def thirdClick(self):
        self.label.setText("세번째 화면~~")

#모듈을 직접 실행했는지를 체크:진입점(Entry Point)
if __name__ == "__main__":
    #실행 프로세스 생성
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()