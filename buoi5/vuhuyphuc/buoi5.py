'''def function(a):
    return a+5
    


a = function(20)+4
'''


'''
def test(a):
    for i in range(a):
        return i


def test2(a):
    b= a+1
    c= a+2
    d=a +20
    return [a,b,c,d]

print(test2(10))
'''


'''
- khai báo 1 hàm nhận 2 giá trị
giá trị đầu tiên là list, giá trị thứ 2 là một số tự nhiên nhỏ hơn độ dài của list

result = []

lặp qua list
for i in list:

'''

def chinhhop(List, a):
    result =[[x,y,z] for x in List for y in List for z in List]
    print(result)

chinhhop([1,2,3,4],3)
    
