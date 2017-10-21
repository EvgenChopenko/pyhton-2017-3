"""
поток ввода
input()
print()
stderr() --- ошибок интерпретатора
sys.stdin,/// stdout /// stderr
#файл работа с файлом


open(filename,mode)
режим
w - перезаписи (файл создаеться если его нет , перезапись файла)
a -append до запись запись проиходит в конец файла
x- созаеться файл если нет.. если нет то exseption


exist - проверка на наличие


close()

"""
# как открыть файл в режими записи
f=open("out.txt","w")
f.write("mother clear windows")
f.write("\r")
f.write("dfasdf")
f.close()

f=open("out.txt")
print("как прочитать файл в стороку\n ")
content=f.read()
f.seek(0)# смещение в байтах от начала файла
print(content)
content=f.readlines()

print(content)
f.seek(0)

content=f.readline()
print(content)

for line in f:
    print(line.strip())#удляем пустоту "

print(f.read(4))# кол-во байтов
# позиция курсора f.tell()--- вернет байт символа

f.close()



"""
режим a+ до запись

t- текстовый режим-> out.txt('out.txt','wt')
b- bin режим open(1.mp3,'rb')
 

"""


# менеджер контекста
with open('out.txt') as ff:
    content2 = f.read()
    print(content2)

#print("ff=",ff)
print(content2)
