from re import U
from select import select


my_list = [10,20,30,40,50,60,70,80,90,100]
for i in my_list:
    print (i)

for i in "abc" :
    print (i)
    print (i+"1")

for x in range(10) :
    print (x)


for y in range(5, 10) :
    print (y)


user1 = {"name": "Le Quoc Thong","id": 1,"email": "quocthong@gmail.com", "password": "quocthong"}
user2 = {"name": "Le Anh Thu","id": 2,"email": "lean@gmail.com", "password": "anh Thu"}
user3 = {"name": "Le Van Thuan", "id": 3,"email":"vanthuan@gmail.com", "password": "vanthuan"}

mydata=[user1, user2, user3]



selected_user = {}
for user in mydata:
   if "id" in user:
        if user["id"] == 2:
            selected_user=user
print (selected_user)            
        