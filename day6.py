from distutils.command.build_scripts import first_line_re
from socket import MsgFlag


my_string = "hello, my name is Le Quoc Thong"
print(my_string)

name = "Steven Lee  "
my_string = f"hello, my name is {name}"
print(my_string)


names = ["thuan", "thuy", "thong", "thu"]
for name in names:
       
    print(f"hello, my name is {name}")

msg= """Dear {name}
    My name is steven Lee
    I came from vinh long"""
print(msg)

for i in names:
   
    msg = """Dear, {name},
                My name is steven Lee
                I came from vinh long"""
    msg=msg.format(name=i)
    print(i)
    print(msg, "\n")

x =3.14578891255

pi= "{} is ".format(x)
print(pi)

pi = "{:.2f} is ".format(x)
print(pi)


