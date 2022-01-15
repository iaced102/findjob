from math import *

a= int(input ("nhap gia tri a :")) 
print(a)
b= int(input ("nhap gia tri b :"))
print(b)
c= int(input ("nhap gia tri c :"))
print(c)
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
    if delta < 0 :
        print ("phuong trinh vo nghiem")
    
