# DemoForm.py(로직 코딩) + DemoForm.ui(화면을 XML문서 저장)
import sys 
from PyQt5.QtWidgets import *
from PyQt5 import uic 

#디자인 문서를 로딩
form_class = uic.loadUiType("DemoForm.ui")[0]
#윈도우 클래스 정의
class DemoForm(QDialog, form_class):
    #초기화 메서드
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 화면")
#모듈을 직접 실행했는지를 체크: 진입점(Entry point)
if __name__ == "__main__":
    #실행 프로세스 생성
    app = QApplication(sys.argv)
    #폼 실행
    demoForm = DemoForm()
    #화면 보여주기
    demoForm.show()
    app.exec_()