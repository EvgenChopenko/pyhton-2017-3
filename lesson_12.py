#todo: OOP



class Person():
    pass


person_1= Person()
print(person_1)

# todo: Метод - функция в классе

class Person():
    def __init__(self,firtname,lastname):
        """
        Мagic metod -конструктор
        основная функция иницилизировать обьект
        self - cылка на текуший экземпляр и обьект
        """
        self.firstname = firtname
        self.lastname = lastname


person_2=Person('пупкин','валера')

class Point():
    def __init__(self,x,y):
        self.x = x
        self.y=y
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_Point(self):
        return Point(self.x,self.y)

    def set_x(self,x):
        self.x=x
    def set_y(self,y):
        self.x=y

point_10_20 = Point(10,20)

class OrderExsept(Exception):
    pass

class Product(object):
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def get_prise(self):
        return self.price

class Order(object):
    def __init__(self,person):
        self.person = person
        self.products=[]


    def add_product(self,product):
        if not isinstance(product,Product):
            raise OrderExsept('это не продукт')
        self.products.append(product)
    def get_total_prise(self):
        return sum(i.get_prise() for i in self.products)
# todo: static

class Factory(object):
    instances = {}


    #@staticmethod
    @classmethod
    def get_instance(cls,name,*args,**kwargs):
        if name not in cls.instances:
            cls.instances[name]=cls(*args,**kwargs)

        return cls.instances[name]


print(Factory.get_instance('hkjhlk'))