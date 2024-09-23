class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"


house1 = House('ЖК Эльбрус', 30)
house2 = House('ЖК Акация', 20)
print(house1)
print(house2)
print(len(house1))
print(len(house2))
