

import email
from re import A


if True :
    print ("this is true")
if False :
    print ("notthing ")
if not False :
    print ("This is not false")

my_string = str("LE QUOC THONG").lower()
print (my_string)

print (my_string.title())

abc = [1, 2, 3, 4, 5]
new_abc = []
for i in abc :
    i= i**2
    new_abc.append(i)
print (new_abc)

is_even = []
is_old = []
for i in new_abc :
    if i%2 == 0 :
        is_even.append(i)
    else:
        is_old.append(i)
print (is_even)
print (is_old)

