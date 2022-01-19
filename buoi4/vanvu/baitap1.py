def so_chinh_phuong(a):
    a = int(input())
    b=0
    for i in range(a+1):
        if i**2 == a:
            b=1
            break
    if b==1:
        print(a, "la so chinh phuong")
    else:
        print(a, "khong la so chinh phuong") 

so_chinh_phuong(5)  
