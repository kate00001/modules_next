class House:
    def __init__(self, name, number_of_floors):
        if isinstance(number_of_floors, int):
            self.name = name
            self.number_of_floors = number_of_floors
        else:
            print("Число этажей должно быть целым числом")

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

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
        value = 5
        self.number_of_floors += value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)


house1 = House('ЖК Эльбрус', 20)
house2 = House('ЖК Акация', 25)

print(house1)
print(house2)

print(len(house1))
print(len(house2))

print(house1 == house2)
print(house1 < house2)
print(house1 <= house2)
print(house1 > house2)
print(house1 >= house2)
print(house1 != house2)

print(house1 + 5)
print(5 + house1)
print(house1)
