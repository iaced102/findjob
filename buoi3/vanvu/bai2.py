A=[1, 20, 19, -36, 54, 17, 89, 108, -82, 30]

for i in range(len(A)):
    min = i
    print(min)
    for j in range(i+1, len(A)):
        if A[j] < min :
            min = j
        tg = A[min]
        A[min]= A[i]
        A[i]=tg
print("\nMang sap xep theo thu tu tang dan: ")  
print(A)      
