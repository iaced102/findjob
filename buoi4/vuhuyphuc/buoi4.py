# function
'''
truyền parameter vào hàm bằng 2 cách
1 là theo vị trí
2 là theo keyword
*note: nếu truyền 1 giá trị theo vị trí, thì tất cả các giá trị sau đó phải truyền theo vị trí
*note: default argument phải là những giá trị cuối cùng
position argument -> nếu có thì phải được khai báo, truyền đầu tiên
default argument -> ngay sau position arguments
keyword argument -> cuối cùng
'''

'''
viết một hàm kiểm tra số chính phương
kiểm tra xem số a có phải số chính phương hay không
- có 1 số a
lặp x từ 1 đến a/2 (nhớ ép kiểu cho a/2)
nếu x**2 ==a
=> a là số chính phương
def tenham(a)
'''



def sochinhphuong(a):
    check = 0
    for i in range(int(a/2)+1):
        if i**2 ==a:
            check =1
            break
    if check ==1:
        print(a, ' la so chinh phuong')
    else:
        print(a, ' khong phai so chinh phuong')

#sochinhphuong(4)



dicts = {
    'dog': 'chó',
    'cat': 'chuột',
    'mouse': 'mèo'
}


def in_ra(a):
    print(a)


def test(**dicts):
    for a in dicts:
        print(dicts[a])


def test2(*args):
    for a in args:
        print(a)

def sample(position, *args, default=5, **kwargs):
    print(position)
    print(default)
    print(args)
    print(kwargs)



'''
viết một hàm có 2 parameter 
parameter 1: chuỗi cơ sở (t)
parameter 2: chuỗi phân cách (o)

mô phỏng split
khởi tạo 1 list rỗng vd: a=[]
khởi tạo 1 index =0
lặp qua chuỗi (i) for i in range(len(t))
nếu vị trí lặp của t == o
chúng ta sẽ append t[index: i]
index = i+1 
'''