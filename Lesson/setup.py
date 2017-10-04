from setuptools import setup
"""
name -название пакета 
пакеты packages которые необходимо скопировать без рекурсии
# кроме пакетов можно распростронять можно модули py_modules 
install_requires - Прямые зависимости от других пакетов 
scripts - Запускаемые с командной строки скрипты 
"""


setup(

    name='--init--',
    version='1.01.05',
    description='TeST',
    url='https://www.google.com',
    license='Apache License 2.0',
    author="Chopenko E.G",
    author_email="evgen.chopenko@yandex.ru",
    packages=['__init__'],


)