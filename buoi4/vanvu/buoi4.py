from ast import Break


A=[1,3,5,7,9.25,28,40,32,50,29]

for a in range(len(A)):
    if A[a]%2==0:
        print("\nphan tu dau tien chia het cho 2:", A[a])
        break