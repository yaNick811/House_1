class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        self.current_floor = 1
        self.numberOfFloors = 0
    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            print(new_floor)
        else:
            print('Такого этажа не существует')

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(self.numberOfFloors)


Elbrus = House('ЖК Эльбрус', 30)
Dogma = House('ЖК Догма', 72)
print(Elbrus.name, Elbrus.number_of_floors)
print(Dogma.name, Dogma.number_of_floors)

Elbrus.go_to(6)
Elbrus.go_to(32)
Dogma.go_to(54)
Dogma.go_to(99)

print(Elbrus.name, Elbrus.numberOfFloors)


