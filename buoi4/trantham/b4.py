# a=[1, 10, 8, 20, 31, 52,17, 24,9]

# for i in a:
#     if i % 2 ==0 :
#         print("Phan tu dau tien chia het cho 2 la: ", i)
#         break


def scp() :

    print("\n\nKiem tra so chinh phuong")
    a = int(input("\nNhap vao 1 so nguyen: "))
    check = False
    for i in range(1, a+1) : 
        if i*i == a :
            check = True
            break
        else :
            check = False
    if check == True :
        print(str(a) + " la so chinh phuong")
    else :
        print(str(a) + " khong la so chinh phuong")
scp()