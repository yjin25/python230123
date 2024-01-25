# DemoRE.py
#정규표현식: 특정한 패턴을 검색
import re

#전체를 검색
result = re.search("[0-9]*th","35th")
print(result)
print(result.group())

#정확하게 일치
# result = re.match("[0-9]*th","35th")
# print(result)
# print(result.group())

# \d digit 숫자가 연속으로 n자리
result = re.search("\d{4}", "올해는 2024년입니다.")
print(result.group())

result = re.search("\d{5}", "우리 동네는 52100입니다.")
print(result.group())

result = re.search("apple", "this is apple")
print(result.group())