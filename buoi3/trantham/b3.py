#Them phan tu vao mang

'''
h= []
h.append(10)
print(h)
for i in range(100) :
    if i%2==0:
        h.append(i)
print(h)

'''

# a = [i*i for i in range(10) if i%2==0]
# print(a)

#Mang 2 chieu

'''
a=[ [1,2, [9,10]] , [3,4], [5,6], [7,8] ]
print(a)

for i in a:
    print(i)

'''



#lay list con
'''
A=[1, 10, 8, 20, 31, 52,17, 24,9]
A[0:3]

'''

#Tim min:
'''
A=[1, 10, 8, 20, 31, 52,17, 24,9]
min =A[0]
for i in range(1,len(A)):
    if A[i]<min:
        min=A[i]
'''


#sap xep tang dan (sx lua chon):

from operator import le
from re import L
from turtle import left, right


a=[1, 10, 8, 20, 31, 52,17, 24,9]
for i in range(0,len(a)-1) :
    min = i
    for j in range(i+1, len(a)):
        if a[j]<a[min] :
            min=j
        tg = a[min]
        a[min] = a[i]
        a[i] = tg
print("\nMang sap xep tang: (luachon)")
print(a)

#sap xep tang dan (sx noi bot):

a=[1, 10, 8, 20, 31, 52,17, 24,9]
for i in range(0, len(a)-1) :
    for j in range(0, len(a)-i-1):
        if a[j]>a[j+1] :
            tg = a[j]
            a[j] = a[j+1]
            a[j+1] = tg
print("\nMang sap xep tang:(noibot)")
print(a)

#sap xep tang dan:(sx chen)

a=[1, 10, 8, 20, 31, 52,17, 24,9]
for i in range(1, len(a)) :
    tam = a[i]
    j = i-1
    while j>=0 and a[j]>tam :
        a[j+1] = a[j]
        j=j-1
    a[j+1] = tam
print("\nMang sap xep tang: (chen)")
print(a)

#sap xep tang dan (sx phan doan):
# a = []
# left
# right
# n = int(input("Nhap so phan tu cua mang: "))
# for i in range(n) :
#     a.append(input("Nhap so thu a[%d] = " % (i+1)))
# print("Mang vua nhap la: ", a)
    
# if left < right :
#     k = (left + right)/2
#     t=a[k]
#     i = left
#     j = right
#     while i<=j :
#         while (a[i]<t): 
#             i=i+1
#         while (a[j]>t): 
#             j=j-1
#         if i<=j:
#             tg = a[i]
#             a[i] = a[j]
#             a[j] = tg
#             i = i+1
#             j = j-1






#kiem tra so chinh phuong

print("\n\nKiem tra so chinh phuong")
a = int(input("\nNhap vao 1 so nguyen: "))
check = False
for i in range(1, a+1) :
    if i*i == a :
        check = True
        break
    else :
        check = False
if check == True :
    print(str(a) + " la so chinh phuong")
else :
    print(str(a) + " khong la so chinh phuong")

#Nhap-xuat mang 1 chieu
'''
a = []
n = int(input("Nhap so phan tu cua mang: "))
for i in range(n) :
    a.append(input("Nhap so thu a[%d] = " % (i+1)))
print("Mang vua nhap la: ", a)

m = int(input(">>m = "))
Myarray = list(range(m))
print("Mang vua nhap: ", Myarray)

'''
