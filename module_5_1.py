class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(f"Этаж {floor}")
        else:
            print("Такого этажа не существует")

house = House('ЖК Эльбрус', 30)
house.go_to(8)  # Приезжаем на 5-й этаж
house.go_to(100)  # Проверяем этаж, которого нет