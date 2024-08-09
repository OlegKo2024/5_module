print('Первый вариант')
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self.number_of_floors            # нужно ли включать return и без return работает?
                                                    # и почему, при установке return в строку суммирования не работает
    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            # return self.number_of_floors

    def __radd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            # return self.number_of_floors


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

h1.__str__()
h2.__str__()
print(h1)
print(h2)

print(len(h1))
print(len(h2))

print(h1)
print(h2)
print(h1 == h2)

h1.__add__(10)      # как я понял при передаче значения в функцию нет разницы по применению методов __add__ __iadd__ или __radd__
print(h1)
print(h1 == h2)

h1.__iadd__(10)
print(h1)

h2.__radd__(10)
print(h2)
print(h1 == h2)

print(h1 < h2)
print(h1 <= h2)
print(h1 > h2)
print(h1 >= h2)
print(h1 != h2)


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
            self.number_of_floors += value        # add и опять, нужен ли return?
# For instance, to evaluate the expression x + y, where x is an instance of a class that has an __add__() method,
# type(x).__add__(x, y) is called. type(x) - в документации это то, что мы называем объектом, если так, то мы не пишем
# таким образом код. По документации нужно бы пройтись для примера для понимания, английский не всегда помогает.

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value        # iadd, как я понял, вне зависимости от метода мы везде пишем
# одинаково: self.number_of_floors += value, разница только в том, как вызываем действия.

    def __radd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value        # radd


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
