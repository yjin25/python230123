# ifelse.py
# score = int(input("점수를 입력"))

# if 90 <= score <= 100:
#     grade = "A"
# elif 80 <= score < 90:
#     grade = "A"
# elif 70 <= score < 80:
#     grade = "A"
# else:
#     grade = "D"

# print("등급은 ", grade)

print("---반복구문---")
value = 5
while value > 0:
    print(value)
    value -= 1

print("---for in---")
lst = ["문자열", 100, 3.14]
for item in lst:
    print(item, type(item))

lst = list(range(1,11))
print(lst)
for item in lst:
    print("Item:{0}".format(item))

print("---break---")
lst = list(range(1,11))
print(lst)
for item in lst:
    if item > 5:
        break
    print("Item:{0}".format(item))

print("---continue---")
lst = list(range(1,11))
print(lst)
for item in lst:
    if item % 2:
        continue
    print("Item:{0}".format(item))


print("---리스트 내장---")
lst = list(range(1,11))
print([i**2 for i in lst if i > 5])
tp = ("apple", "orange", "kiwi")
print(len(i) for i in tp)