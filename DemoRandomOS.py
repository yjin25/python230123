# DemoRandomOS.py

import random
from os.path import * 
import glob

print(random.random())
print(random.random())
#리스트 내장
print([random.randrange(20) for i in range(10)])
print([random.randrange(20) for i in range(10)])
#유니크 샘플 생성
print(random.sample(range(20), 10))
print(random.sample(range(20), 10))

lotto = list(range(1,46))
random.shuffle(lotto)
print(lotto)

print("---파일 다루기---")
print(abspath("python.exe"))
print(basename("C:\\Users\\SON YOUNGJIN\\AppData\\Local\\Programs\\Python\\Python310\\python.exe"))

fName = "C:\\Users\\SON YOUNGJIN\\AppData\\Local\\Programs\\Python\\Python310\\python.exe"

if exists(fName):
    print("파일의 크기:{0}".format(fName))
else:
    print("파일이 없음")