'''
A=[1, 20, 19, -36, 54, 17, 89, 108, -82, 30]
sắp xếp mảng A theo thứ tự tăng dần

- tìm giá trị nhỏ nhất trong khoảng từ A[0: len(A)]
đổi vị trí giữa A[0] và giá trị nhỏ nhất
- tìm giá trị nhỏ nhất trong khoảng từ A[1: len(A)]
đổi vị trí giữa A[1] và giá trị nhỏ nhất trong khoảng
.......

lặp theo vị trí chứ không lặp theo giá trị

'''
A=[1, 20, 19, -36, 54, 17, 89, 108, -82, 30]
for i in range(len(A)):
    min = A[i]
    a = i
    for b in range(i, len(A)):
        if A[b] < min:
            min = A[b]
            a = b
    A[i], A[a] = A[a], A[i]
    print(A)