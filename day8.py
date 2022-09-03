import requests
from requests import get
from day7 import  format_msg2
from datetime import datetime
print(datetime.now())

def send(name,address=None):
    if address != None:
         msg =format_msg2(my_name=name,my_address=address)
    else:
        msg =format_msg2(my_name=name)

    r=requests.get("http://httpbin.orrg/json")   
    if r.status_code == 200:
        return r.json() 
    else:
        print("there was an error")
   
send("thongle","Ha Noi")





