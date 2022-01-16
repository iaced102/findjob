#tìm giá trị nhỏ nhất của mảng

A=[1, 20, 19, -36, 54, 17, 89, 108, -82, 30]
min = A[0]
for i in A:
    if i < min:
        min = i
print("gia tri nho nhat cua mang la:",min)