A=[1, 20, 19, -36, 54, 17, 89, 108, -82, 30]

for i in range(len(A)):
    min = A[i]
    index_min = i
    for j in range(i, len(A)):
        if A[j] < min :
            min = A[j]   
            index_min  = j
print("\nMang sap xep theo thu tu tang dan: ")  
A[i], A[index_min] = A[index_min], A[i]
print(A)      
