# Декораторы

def lst(*args,**kwargs):
    print(type(args))
    print(type(kwargs))

lst()


def func():
    def wrapper():
        pass
    return wrapper

f = func()

f()
from  urllib.request import urlopen

def page(url):
    def get():
        return urlopen(url).read()
    return get
python = page('https://vk.com/')



print(python())


def factorial(n):
    f= 1

    for i in range(1,n+1):
        f*=i
    return f
import time

def benchmark(func,*args,**kwargs):
    started = time.time()
    result = func(*args,**kwargs)
    worked = time.time() - started

    print ('Функ{},{}'.format(func.__name__(),worked))
    return  result
print('')

