# форматы данных
"""
#pickle отстой
#
#

"""

import pickle # cpickle pyhton (->six  совместитель 2.6 -->>3

data={
    'users':[
        {
            'id':1,
            'name':"linus Torvald",
            'skills':('c++','c')
        },
        {
            'id':1,
            'name':"Richrd_Stalmab",
            'skills':('C','GNU')
        }
    ]


}

with open('user.pickle','wb')as f:
    pickle.dump(data,f,)


with open('user.pickle','rb') as f:
    print(pickle.load((f)))
# JSON - javaScript Object Notation

import json
# нет понятия кортетж
with open('user.json','w') as f:
    json.dump(data,f,indent=4)

with open('user.json') as f:
    print(json.load(f))


# CSV

import csv
"""
"id;name;skills"
"1;Linus Torvald;c,c++"
"2;Richrd Stallman;c,GNU"

"""

with open('users.csv','w') as f:
    users=data.get('users',[])
    fieldnames=users[0].keys()

    writer= csv.DictWriter(f,
                           fieldnames=fieldnames)
    writer.writeheader()

    for users in users:
        writer.writerow(users)


with open('users.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
# ini,conf , xml (lxml)? beutifol soup
#xps

### data base

# SQLite 3  - Баз данных


# сокрашатель сыллок

