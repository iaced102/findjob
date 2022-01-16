from math import *
a = int(input("nhap gia tri cua a:"))
b = int(input("nhap gia tri cua b:"))
c = int(input("nhap gia tri cua c:"))

if (a==0)
    if (b==0)
    print("pt ko co nghiem");
    else
    print("pt co nghiem la x=", (-c / b));
delta = b**2 - 4*a*c
if a==0 :
    print ("phuong trinh co 1 nghiem x=" +str(x))
else :
    if delta > 0 :       
        print("phuong trinh co 2 nghiem phan biet :")
        x1= (-b + sqrt(delta)) / (2*a) 
        x2= (-b - sqrt(delta)) / (2*a)
        print ("x1 = " +str(x1))
        print ("x2 = " +str(x2))
    else :
        x3 = -b /(2*a)
    print ("phuong trinh co nghiem kep x = " +str(x3))
    else delta < 0 :
        print ("phuong trinh vo nghiem")
    