from math import *
a = int(input(" nhap gia tri a"))
b = int(input(" nhap gia tri b"))
c = int(input(" nhap gia tri c"))

if a==0 :
    print(" pt co mot nghiem duy nhat: x=", (-c/b))
else:
    delta= b**2 -4*a*c
    if delta==0:
        print(" pt co ngiem kep: x=", -b/(2*a))
    elif delta<0:
        print("PTVN")
    else:
        print("pt co hai nghiem: x=")
        print("x1=",(-b+sqrt(delta))/(2*a))
        print("x2=",(-b-sqrt(delta))/(2*a))

