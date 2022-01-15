from math import *

'''
nhập 3 số a b c từ bàn phím
giải phương trình bậc 2 dạng
ax^2 + bx +c = 0
'''

a = int(input("nhập giá trị a: "))
b = int(input("nhập giá trị b: "))
c = int(input("nhập giá trị c: "))

if a==0:
    print("phương trình bậc 1 có nghiệm duy nhất: x= ", (-c/b))
else:
    delta = b**2 - 4*a*c
    if delta == 0:
        print("phương trình có nghiệm kép: x=",-b/(2*a))
    elif delta <0:
        print("phương trình vô nghiệm")
    else:
        print("phương trình có nghiệm kép:")
        print("x1= ", (-b- sqrt(delta))/(2*a) )
        print("x1= ", (-b+ sqrt(delta))/(2*a) )
    