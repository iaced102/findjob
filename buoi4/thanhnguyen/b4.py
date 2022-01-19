A=[1, 20, 19, -36, 54, 17, 89, 108, -82, 30]
for i in range(len(A)):
    min = A[i]
    index= i
    for b in range(i+1,len(A)):
        if A[b]< min :
            min= A[b]
            index=b
    A[i],A[index]=A[index],A[i]
    print("ket qua sap xep la")
    print(A)
     


