class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        new_floor = int(new_floor)
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                if new_floor <= self.number_of_floors:
                    print(i)

    def __gt__(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            return 'Такого этажа не существует'
        else:
            for i in range(1, new_floor + 1):
                print(i)

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
            return self.number_of_floors

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self.number_of_floors

    def __radd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self.number_of_floors

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

h1.go_to(5)
h2.go_to(10)

# h1.__gt__(0)
# h2.__gt__(2)

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

h1.__add__(10)
print(h1)
print(h1 == h2)

h1.__iadd__(10)
print(h1)

h2.__radd__(10)
print(h2)

print(h1 < h2)
print(h1 <= h2)
print(h1 > h2)
print(h1 >= h2)
print(h1 != h2)
