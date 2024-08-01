class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        new_floor = int(new_floor)
        if new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            i = 1
            while i <= new_floor:
                print(i)
                i += 1

    def go_to_(self, new_floor):
        new_floor = int(new_floor)
        if new_floor > self.number_of_floors:
            return print('Такого этажа не существует')
        for i in range(1, new_floor + 1):
            if new_floor <= self.number_of_floors:
                print(i)

    def _go_to_(self, new_floor):
        new_floor = int(new_floor)
        if new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                if new_floor <= self.number_of_floors:
                    print(i)

    def __gt__(self, new_floor):
        if new_floor > self.number_of_floors:
            return 'Такого этажа не существует'
        else:
            for i in range(1, new_floor + 1):
                print(i)

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)

h1.go_to_(5)
h2.go_to_(10)

h1._go_to_(6)
h2._go_to_(10)

h1.__gt__(18)
h2.__gt__(2)
