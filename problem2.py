
###Question: 7x-12y+20=0 এবং 7x-12y+13=0 সমান্তরাল সরলরেখাদ্বয়ের মধ্যবর্তী লম্ব দূরত্ব নির্নয় কর।

# distance = |c1 - c2|/ root(a*a + b*b)

import math

print("Problem Number: 01")
print("7x-12y+20=0 এবং 7x-12y+13=0 সমান্তরাল সরলরেখাদ্বয়ের মধ্যবর্তী লম্ব দূরত্ব নির্নয় কর।")

print("Answer:")

#given value
l1 = "7x-12y+20=0"
l2 = "7x-12y+13=0"
c1 = l1[7:9]
c2 = l2[7:9]
a = l1[0]
b = l2[2:5]
difference = int(c1) - int(c2)
if difference < 0:
    new_difference = difference + 2*difference
elif difference > 0:
    new_difference = difference
a = int(a)
b = int(b)
rooted_part = math.sqrt(a*a + b*b)

result = new_difference / rooted_part

from decimal import Decimal
from fractions import Fraction
print(f"""
|---------------------------------------------------|
|Answer: {Fraction(Decimal(str(result)))} |
|Answer: {result} |
|Manp. Ans : 7 ÷ √193 |
|---------------------------------------------------|""")
