import Module_Dictionary
import math
import requests
import numpy as  np

Module_Dictionary.add(1,"Ronish")
Module_Dictionary.add(2,"Ronish1")
val=Module_Dictionary.get(1)
print("Name : ",val)
Module_Dictionary.print_dic()
print(dir(math)) #list all the name defind in the module

response_code=requests.get("http://localhost:8000/student/getall")
print(response_code.status_code)
print(response_code.text)
print(response_code.content)
print(type(response_code.text))
data=response_code.json()
for student in data:
   for key,val in student.items():
    print(f'key : {key} ,val : {val}')
   print()

arr=np.array([1,2,3,4,5])
print(arr)