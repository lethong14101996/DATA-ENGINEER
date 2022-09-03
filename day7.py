


def my_print(txt):
    print(txt)
my_print("hello world")

msg_template = """Dear {name},
MY NAME IS STEVEN LEE
I CAM FROM {address}"""

def format_msg(my_name="thong ", my_address="vinh long"):
    msg_message = msg_template.format(name=my_name, address=my_address)
    print(msg_message)
    return msg_message
format_msg()


def format_msg(my_name, my_address):
    msg_message = msg_template.format(name=my_name, address=my_address)
    print(msg_message)
    return msg_message
format_msg("thu le","HCM")

name = ["thuan","thuy","thong","thu"]
for i in name:
    format_msg(i, "vinhlong \n")







