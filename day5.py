



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

x =10
i = 0
while i < x:
    print(i)
    i += 1


x= 10
i = 0  
z = 12
while i < x:
    z = z*2
    if z > 342900:
        break
    print (z,i)
    i=i+0.000000001



x = 100 
i = 0
while i < x:
    i= i+1
    if i %2 == 0:
        print(i, "IS EVEN")
        continue
        if i == 50:
            break
    else:   
        print(i, "IS ODD")
