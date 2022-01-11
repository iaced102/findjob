#số thập phân (độ chính xác 15 số sau dấu "," )
"""
a=5.1
"""

# số thập phân, độ chính xác xác định
'''

from decimal import *
getcontext().prec = 20
a = Decimal(10)/3
 '''


# phân số
'''

from fractions import *

a= Fraction(10,3)
print(a)
print(a+3)
'''


#số thực
'''

b = complex(10,5)

print(b + complex(3,10))

print(b.real)
print(b.imag)'''