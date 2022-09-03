


import email


a = [ 10,20,30,40,50,60,70,80,90]
print (sum(a))
a.append(100)
print (sum(a))

print(a[2] )

my_data = {"name": "Le Quoc Thong", "location": "Vinh Long"}
print (my_data["location"])
print (my_data.keys())
my_data["score"] = 10
print (my_data)

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
