
print('Классы и объекты')
"""
Класс можно представить как некую инструкцию. На ее основе создаются объекты. Для того чтобы создать класс, 
нам достаточно написать ключевое слово class. После него пишем непосредственно название нашего класса."""
class Human:                        # наш КЛАСС - собствен. тип данных у которого есть свои способности и характеристики
    def __init__(self):             # прописываем уникальные способности объектов, эти функции называют методами
        self.name = 'Den'           # переменные внутри класса называют характеристиками или атрибутами
        # таким образом у нас есть метод __init__ внутри которого определена характеристика name, со значением Den


den = Human()
max = Human()

print('Объекты разные')
print(den == max)       # False
print(den is max)       # False
print(id(den), id(max)) # разные ID

print('Имена после ввода характеристики name')

print(den.name, max.name)   # Den Den

class Human:
    def __init__(self, name):       # чтобы дать разные имена добавить name
        self.name = name

den = Human('Den')
max = Human('Max')

print(den.name, max.name)           # Den Max - ok

print('Атрибуты и методы объекта. Указатель на свой объект в методах')
"""
Методы - т.е функции наших объектов - это способности, то, что умеет делать наш объект
Атрибуты - т.е характеристики - это уникальные черты наших объектов
Объект - переменная созданная на основе класса
Класс - инструкция, описывающая способности и характеристики объектов"""

print('Атрибуты')
class Human:                            # обязательно
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say_info(self):
        print(f'I am {self.name}, of {self.age}, my surname is {self.surname}')

den = Human('Den', 23)
max = Human('Max', 24)

print(den.name, den.age, max.name, max.age)         # Den 23 Max 24

den.surname = 'Ko'                                  # добавление атрибутов в процессе, но тут только для den
print(den.surname)                                  # Ko
print(den.name, den.age, den.surname)               # Den 23 Ko - добавленный атрибут вкл. - ок

den.age = 20                                        # изменение атрибутов
print(den.name, den.age, den.surname)               # Den 20 Ko

print('Методы')
# методы должны располагаться под классом

den.say_info()                                      # I am Den, of 20, my surname is Ko

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.say_info()                 # в одном методе __init__ можем вызывать другой метод

    def say_info(self):
        print(f'I am {self.name}, of {self.age}')

    def birthday(self):
        self.age += 1
        print(f'Мне {self.age}')

den = Human('Den', 23)
max = Human('Max', 24)

# I am Den, of 23                       # в одном методе __init__ можем вызывать другой метод
# I am Max, of 24

# после добавления birthday
den.birthday()                          # Мне 24
den.say_info()                          # I am Den, of 24
max.birthday()                          # вызов и Мне 25 - изменили значение атрибута
max.say_info()                          # I am Max, of 25 - берется последнее определение класса

print('Специальные методы классов')
"""
Методы с двойным подчеркиванием называются специальными или магическими методами double under
"""

print('Метод деструктор')
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.say_info()                 # в одном методе __init__ можем вызывать другой метод

    def say_info(self):
        print(f'I am {self.name}, of {self.age}')

    def birthday(self):
        self.age += 1
        print(f'Мне {self.age}')

    def __del__(self):
        print(f'{self.name}, удален')

den = Human('Den', 23)
max = Human('Max', 24)
den.birthday()
"""
Имя den вело нас на объект класса Human, который содержал атрибуты name и age
когда ссылки заканчиваются, объекты исчезают - это деструктор
"""

print('Метод измерения кол-ва')

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.say_info()                 # в одном методе __init__ можем вызывать другой метод

    def say_info(self):
        print(f'I am {self.name}, of {self.age}')

    def birthday(self):
        self.age += 1
        print(f'Мне {self.age}')

    def __len__(self):                  # добавили метод __len__
        return self.age                 # который будет возвращать возраст

    def __del__(self):
        print(f'{self.name}, удален')

den = Human('Den', 26)
max = Human('Max', 27)

print(len(den))                         # 26
"""
Не зря магические так как мы можем используя большое кол-во специальных методов реализовывать спец. логику по 
созданным нами объектам, как в примере с методом __len__ мы выхвали характеристику возраста

Также ссылка на документацию: https://docs.python.org/3/reference/datamodel.html#basic-customization
в которой можно будет прочитать некоторые особенности по отношению этих методов."""

print('Перегрузка')
"""
Есть встроенные операторы, используемые по отношению к другим типам + - / ...
но мы можем изменить поведение этих операторов по отношению к нашим объектам - это и называется перегрузка"""

print('Спец. метод __ly__ - сравним возраст человеков')
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.say_info()

    def __str__(self):
        return f'{self.name}'

    def say_info(self):
        print(f'I am {self.name}, of {self.age}')

    def birthday(self):
        self.age += 1
        print(f'Мне {self.age}')

    def __len__(self):
        return self.age

    def __lt__(self, other):                        # lt = lower than, gt - greater then
        return self.age < other.age                 # перегрузили оператор сравнения меньше

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __bool__(self):
        return bool(self.age)                       # !!! проверка истинно или ложно: по возрасту !!!

    def __del__(self):
        print(f'{self.name}, удален')

den = Human('Den', 22)
max = Human('Max', 22)
den.say_info()                                      # I am Den, of 22
den.birthday()                                      # Мне 23
den.say_info()                                      # I am Den, of 23

print(den < max)                                    # True

print(den == max)                                   # False - так как не равны ни имена, ни возраст

# print(den)                                        # <__main__.Human object at 0x000002C871767590> - но добавим спец. функцию __str__
print(den)                                          # Den
print(max)                                          # Max





