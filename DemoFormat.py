# DemoFormat.py

for i in range(0,10):
    strURL = "https://www.ycampus.com/?page=" + str(i)
    print(strURL)

print("---왼쪽정렬---")
for x in range(1,6):
    print(x, "*",x,"=",x*x)

print("---오른쪽정렬---")
for x in range(1,6):
    print(x, "*",x,"=",str(x*x).rjust(3))

print("---0으로 채우기---")
for x in range(1,6):
    print(x, "*",x,"=",str(x*x).zfill(10))

print("---서식지정---")
print("{0:x}".format(10)) # hexa decimal
print("{0:b}".format(10))
print("{0:,}".format(15000))
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))
print("{0:.2f}".format(4/3))