A = [1, 20, 19, -36, 54, 17, 89, 108, -82, 30 ]

min = A[0]

for i in A:
    print('i= ',i, 'min =', min)
    if i < min:
        min = i

print(min)