# array=[1,2,3,4,5]
# for i in array:
#     print(i)
# print("\n")
# for i in range(4,10):
#     print(i)
# a = float(input("Nhap he so a: "))
# b = float(input("Nhap he so b: "))
# c = float(input("Nhap he so c: "))
# delta = b*b-4*a*c
# if a==0 :
#     print("Day la phuong trinh bac nhat")
#     x = -c/b
#     print("Phuong trinh co nghiem x = "+ str(x))
# else :
#     if delta > 0 :
#         print("Phuong trinh co 2 nghiem phan biet: ")
#         import math
#         x1 = (-b + math.sqrt(delta)) / (2*a)
#         x2 = (-b -math.sqrt(delta)) / (2*a)
#         print("x1 = " + str(x1))
#         print("x2 = "+str(x2))
#     elif delta < 0 :
#         print("Phuong trinh vo nghiem")
#     else :
#         x3 = -b /( 2*a )
#         print("Phuong trinh co nghiem kep x = " + str(x3))
print("   \n -----------BANG CUU CHUONG------------\n")
for i in range(1,10) :
	print("\nBang Nhan " + str(i) + "\n")
	for j in range(1,11) :
		a=i*j
		print(str(i) + " x " + str(j) +" = "+ str(a))