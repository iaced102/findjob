# a=[1, 10, 8, 20, 31, 52,17, 24,9]

# for i in a:
#     if i % 2 ==0 :
#         print("Phan tu dau tien chia het cho 2 la: ", i)
#         break

#ham kiem tra so chinh phuong:
# def scp() :

#     print("\n\nKiem tra so chinh phuong")
#     a = int(input("\nNhap vao 1 so nguyen: "))
#     check = False
#     for i in range(1, a+1) : 
#         if i*i == a :
#             check = True
#             break
#         else :
#             check = False
#     if check == True :
#         print(str(a) + " la so chinh phuong")
#     else :
#         print(str(a) + " khong la so chinh phuong")
# print(scp())


dicts = {
    'dog' : 'cho',
    'cat': 'meo',
}
'''
print(dicts['dog'])
#xuat keys
print(dicts.keys())
#xuat values
print(dicts.values())
#them vao disct
dicts['fish'] = 'ca'
print(dicts)

def in_ra(a):
    print(a)

in_ra(dicts)

def test(**dicts):
    for i in dicts :
        print(dicts[i])
test(a=3, b=5)

def test2(*args) :
    for i in args :
        print(args)
test2(2,4,5,6)

def sample(position, *args, default = 5, ** kwargs) :
    print(position)
    print(default)
    print(args)
    print(kwargs)
sample(1,2,3,4,5,6, a=10, b=12)
'''
# a='lap trinh python'
# print(a.split())



def demo_split(string, parameter1) :
    result = []
    word = ""
    for i in range(len(string)) :
        if parameter1 == "" :
            result.append(string[i])
        elif parameter1 == "''" :
            result.append(string[i])
        else:
            if string[i] != parameter1 :
                word += string[i]
            else:
                result.append(word)
                word=''
    return result
print(demo_split('xin chao cac ban ', " "))