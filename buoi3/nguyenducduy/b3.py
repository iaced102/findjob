a = int(input())
c = 0
for x in range(a):
    if x**2 == a:
        c = 1
if c == 1:
    print(a," a là số chính phương")
else: 
    print(a," a k là số chính phương")