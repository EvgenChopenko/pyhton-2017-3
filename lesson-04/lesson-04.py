# функциональное програмирование
def hello():
    print('hell')

def passsss():
    pass


#hello()
#Аргуметы функции
def hello(name):
    print("Hello", name)

hello("LOS")#нет перегрузки

def login(user,password):
    print('пользователь {} зашел с паролем {}'
          ''.format(user,password))

login("v","v")


def parse(src,output):
    src=src.strip('.')# удалить символы в начале и в конце
    for w in src.split():
        output.append(w)



src="afasd fa sdfa..."
lst=[]

parse(src,lst)
print(src,lst)



# Аргументы

def pow(x,p=2):
    return x**p

print(
    pow(2),
    pow(3,8)

)

def f(x,l=None):# правильно
    l= l or []
    print(l)
    l.append(x)

f(1)
f(2)
f(3)

# именнованы аргументы [] or []

def func2(x, y):
    return  x- y

print(func2(y=8,x=5))

# переменные колво элементов

def summa (*args):# позиционированый аргумент(turpel) **kwargs - именнованый аргумент(словарь)
    return sum(args)

print(
    summa(1,2,3),
    summa(1,2,3,4,5)
)
login_data = ['user','data']

login(*login_data)


# анонимная функция

lambda x : x**0.5

s= lambda x, y: x*y# кулллллл
print(s(10,2))


# замыкания Функция каррирования

def trim(chars=None):
    def func(s):
        return s.strip(chars)
    return func

trim_spaces=trim()
trim_slashes = trim('/\\|')


print(
    trim_spaces('   hello   ')
)

#trim_spaces("    hello eeee    ")# при вывобде не будет пробелов
#trim_slashes()

# def a()
#b()

#def b()
# a()


# Область видимости и время жизни переменной

#локальные  переменные - функции , класс
# global nonlocal
