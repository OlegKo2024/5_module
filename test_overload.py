class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value


    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value


    def __radd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)
print(h1 == h2)

h1.__add__(10)
print(h1)
print(h1 == h2)

h1.__iadd__(10)
print(h1)

h2.__radd__(10)
print(h2)
print(h1 == h2)

"""
__add__ __iadd__ __radd__ не отличаются, в чем смысл их использования?
"""

print('Второй вариант')
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors + value        # add и нужен ли return?

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value              # iadd

    def __radd__(self, value):
        if isinstance(value, int):
            value + self.number_of_floors        # radd


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)
print(h1 == h2)

h1.number_of_floors = h1.number_of_floors + 10
print(h1)
print(h1 == h2)

h1.number_of_floors += 10
print(h1)

h2.number_of_floors = 10 + h2.number_of_floors
print(h2)
print(h1 == h2)