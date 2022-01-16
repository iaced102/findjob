#Them phan tu vao mang

# h= []
# h.append(10)
# print(h)
# for i in range(100) :
#     if i%2==0:
#         h.append(i)
# print(h)

# a = [i*i for i in range(10) if i%2==0]
# print(a)

#Mang 2 chieu

# a=[ [1,2, [9,10]] , [3,4], [5,6], [7,8] ]
# print(a)

# for i in a:
#     print(i)

#sap xep tang dan:
A=[1, 10, 8, 20, 31, 52,17, 24,9]
min =A[0]
for i in range(1,len(A)):
    if A[i]<min:
        min=A[i]
print("Phan tu nho nhat : " + str(min))