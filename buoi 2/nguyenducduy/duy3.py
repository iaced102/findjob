from math import *

'''
nhập 3 số a b c từ bàn phím
giải phương trình bậc 2 dạng
ax^2 + bx +c = 0
'''
a = int(input("nhập giá trị a: "))
b = int(input("nhập giá trị b: "))
c = int(input("nhập giá trị c: "))
delta = b**2-4*a*c
if a==0:
   if b==0:
       print("phương trình vô nghiệm")
   else:
       print(x=-c/b)    
   if c==0:
       print("phương trình vô số nghiệm")    
if delta >0:
    x1=-b-sqrt(delta)/2*a
    x2=-b+sqrt(delta)/2*a
    print(x1,x2)
else:
     print("pt vô nghiệm")   
     

       
       

