fname = "hello_world.txt"
file_object = open(fname, 'w')
file_object.write('hello world this is day10 in python_operator ')

file_object.close()

with open(fname, 'w') as file_object:
    file_object.write('Hello world again')

with open(fname, 'r') as f:
    print(f.read())