# ветвеление
a=1
b=2

if a>b :
    print('a>b')
elif a == b:
    print ('a=b')
else:
    print ('a<=b')


# тернальный оператор
flag = True

if flag:
    v = 5
else:
    v = 'hell'
# аналогично
v = 5 if flag else 'hell'

# циклы
i= 1
summa = 0
while i < 10:
    summa += i
    i+=1
"""
i = 1 
while i:
    if i == 10:
       break
    elif i = 8:
    continue
    i += 1
    
"""

for n in range(0,20,2):
    print (n,end=', ')


d ={
    "id":1,
    "name": "name"
}

# for key,value in d.items():
#     print(d)
#     print(key,value)
#


# срезы
lst = list(range(20))
print(lst[4])

print(lst[4:7])


lst [1:11:4]# 3 число это шаг
lst[-5:]
lst [-5:-3]
lst [-5::-1]# шаг в обратную сторону
lst[::-1]# перевертыш

strtt="adfasf";
result = []
for i in range(10):
    result.append(i)## склейка строк


    # strtt.join(result) преоброзование списка в строку

#     "::".join()


