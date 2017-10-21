from datetime import datetime
from functools import reduce,wraps
import pickle
import time

# def decorator(func):
#     # Должен вернуть функциию обертку
#     def wrapper(*args,**kwargs):
#         # внутрии должны вызвать декорируемую функцию
#         result= func()
#         return result()
#     return wrapper
#
#
# @decorator
# def tst():
#     pass


def benchmark(func):
    def wrapper(*args,**kwargs):
        started = time.time()
        result = func(*args,**kwargs)
        worked = time.time() - started
        print('Функ{},{:f}'.format(func.__name__,worked))
        return  result
    return wrapper

def factorial(n):
    return reduce(lambda f,x:f*x,range(1,n+1))



print(factorial)


def cache(func):
    """functools .lru_cache"""
    memory={}
    def wrapper(*args,**kwarks):
        key =pickle.dumps((args,sorted(kwarks.items())))
        if key not in memory:
            memory[key] = func(*args,**kwarks)
        return memory[key]
    return wrapper
# декаратор с параметрами
def log(filename):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            template = '''
[{now:%Y-%m-%d %H:%M:%S}] Function: "{func}" called with:
    -> positional arguments: {args}
    -> keyword arguments:    {kwargs}
Returns: {result}
'''
            with open(filename, 'a') as f:
                f.write(template.format(now=datetime.now(),
                                        func='.'.join([func.__module__, func.__name__]),
                                        args=args,
                                        kwargs=kwargs,
                                        result=result))
            return result
        return wrapper
    return decorator

@log("log.txt")
@benchmark
@cache
def factorial(n):
    return reduce(lambda f,x:f*x,range(1,n+1))

factorial(100)
factorial(100)

