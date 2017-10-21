
# coding: utf-8
# todo: iterator

s='Linus Torvalds'
lst=[1,2,3,4,5]
person = {
    'name':'Linus Torval',
    'age':47,
    'is_developer':True
}

# it = iter(s)
#
# print(next(it))

# it = iter(lst)
#
# print(next(it))

# it = iter(person)
#
# print(next(it))
#
# for i in s:
#     print(i)

it = iter(s)
while True:
    try:
        i= next(it)
        print(i)
    except StopIteration:
        break

#todo: Генираторы

def generator():
    print ('Шаг №1')
    yield 1
    print('ШАГ №2')
    yield 2
    print("шаг №3")

gen = generator()
print(type(gen))
print(next(gen))



#todo:coutdown

def countdown(n):
    print('Генератор запустися')
    while n:
        yield n
        n-=1

# for i in countdown(50):
#     print(i)


#pyhton2 xrange , iteritems()
# """
    # "

  # todo: генератор списвков
    """
    [exspresion for item1 in iterable if conditional1
    for item2 in iterable if conditional2
    for item2 in iterable if conditional3
    ...........................
    for itemN in iterable if conditionalN  
    ]    
    """


numbers = [i*i for i in range(5)]
print(numbers)


odd=[i for i in numbers if i%2]
print(odd)

points = [(x,y)for x in range(3) for y in range(3)]
print(points)

lst=[1,1,2,2,3,3]

s = {i for i in lst}
print(s)

keys = ['id','original_url','short_url']
values =[1,'https://python.org','/1']


for k,v in zip(keys,values):
    print(k,v)

data = [

    {
        'id': 1,
        'name':'Linus Torvalds',
        'is_developer': True
    },
    {
        'id': 2,
        'name':'victor victor',
        'is_developer': False
    },
    {
        'id': 2,
        'name':'victor victor',
        'is_developer': False
    }
]

person = {d['id']: d for d in data}
print((person))


# Вырвжение генраторы todo: not turple


points2 = ((x,y)for x in range(3) for y in range(3))## генераторное выражение
print(next(points2))
print(next(points2))
with open(__file__)as f:
    lines = (line.strip() for line in f)
    todos = (s.split('# todo:').pop() for s in lines if s.startswith('# todo:') )

    # print(list(todos))

# todo: Сопраграммы
def coroutine(func):
    def wrapper(*args,**kwargs):
        g = func(*args,**kwargs)
        next(g)
        return g
    return wrapper()

@coroutine
def splitter(delimiter = None):
    print('Генератор готов к присмеру')
    result = None
    while True:
        print('wait.... ',result)
        s = (yield result)
        print(s, result)
        result =s.split(delimiter)

sp = splitter(',')

print(sp.send('a,b,c'))
print(sp.send('1,2,3'))