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
for b in range(len(A)-1):
    min = A[b]
    for c in A[b: len(A)]:
        if c < min :
            min =c 
        A[0],A[b] = A[b],A[0]
print("\nKết quả là:")
print(A)