from math import pi as PI
#from Lesson.square_shapes import *
import Lesson.__init__.square_shapes as sh
def calculation(a):
    return PI*a**2

#print (dir(Lesson.square_shapes))

#print(sys.path)# переменная окружения PYTHONPATH

print(__name__)# имя запускаемого файла

sh.abs3()

if(__name__=='__main__'):
    print("dasfas")

