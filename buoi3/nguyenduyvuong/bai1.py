from re import A, X



'''a= []
a.append(10) #thêm phần tử 10 vào trong mảng


tìm giá trị nhỏ nhất của mảng

A=[1, 20, 19, -36, 54, 17, 89, 108, -82, 30]
'''
A=[1, 20, 19, -36, 54, 17, 89, 108, -82, 30]

for i in range(len(A)):
    min = A[i]
    index_min = i
    print(min)
    for x in range(i,len(A)):
        if A[x] < min:
            min = A[x]
            index_min = x
            print(i, min)
    A[i], A[index_min] = A[index_min], A[i]
    print(A)
print(A)  


