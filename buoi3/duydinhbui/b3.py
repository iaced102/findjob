#nhập 1 số từ bàn phím, kiểm tra xem nó có phải số chính phương hay không
print("nhập số cần kiểm tra:", end = " ")
a = int(input())
b = 0
for x in range(a+1):
    if x**2 == a:
        b = 1
if b == 1:
    print(a, "là số chính phương")
else:
    print(a, "không là số chính phương")