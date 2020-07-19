# |ax + by + c| / root[a*a + b*b]
print("""
-----------------------------------------------------
(3,2) বিন্দু হতে 4x-3y-10 = 0 রেখার লম্ব দূরত্ব নির্নয় কর।
-----------------------------------------------------""")


x = 3
y = -2

eq_sl_str = "4x-3y-10=0"
eq_sl = 4*int(x) - 3*int(y) - 10
if eq_sl < 0:
    eq_slP = eq_sl - 2*eq_sl
elif eq_sl > 0:
    eq_slP = eq_sl
import  math

a = int(eq_sl_str[0])
b = int(eq_sl_str[3])
xy = a*a + b*b


xxy = math.sqrt(xy)
result = eq_slP / math.sqrt(xy)

from decimal import Decimal
from fractions import Fraction
print(f"""
|---------------------------------------------------|
|Answer: {Fraction(Decimal(str(result)))}           |
|Answer: {result}                                   |
|---------------------------------------------------|""")


