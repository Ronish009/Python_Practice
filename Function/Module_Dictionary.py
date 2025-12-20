"""Dictionary Operation"""

dic={}

def add(rolnno,name):
    dic[rolnno]=name

def get(rollno):
    return dic[rollno]

def print_dic():
    for rollno,name in dic.items():
        print(f"rollno : {rollno} name : {name}")