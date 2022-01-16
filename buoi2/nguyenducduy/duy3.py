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
    print("pt có 1 nghiệm duy nhất: x=",(-c/b))
else:
    delta = b**2-4*a*c
    if delta ==0:
        print(" pt có nghiệm kép x=",(-b/(2*a)))
    elif delta <0:
        print("pt vô nghiệm")
    else:
        print("pt có 2 nghiệm: x=")
        print("X1",(-b-sqrt(delta))/(2*a))
        print("X2",(-b+sqrt(delta))/(2*a))

    

       
       

