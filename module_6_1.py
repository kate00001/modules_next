class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False

    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                print(f"{self.name} съел {food.name}.")
                self.fed = True
            else:
                print(f"{self.name} не стал есть {food.name}.")
                self.alive = False
        else:
            print(f"{self.name} не может есть {food}.")


class Plant:
    def __init__(self, name):
        self.name = name
        self.edible = False


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Flower(Plant):
    pass


class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True


dog = Predator('Собакен')
horse = Mammal('Лошадка')
orange = Fruit('Апельсинка')
clover = Flower('Клевер-четырехлистник')

dog.eat(orange)  # Собакен ест апельсинку (съедобно)
dog.eat(clover)  # Собакен ест клевер (несъедобно)
horse.eat(orange)  # Лошадка ест апельсинку (съедобно)

print(f'Жив ли наш собакен? - {dog.alive}')
print(f'Накормлена ли лошадка? - {horse.fed}')
print(f'А жива? - {horse.alive}')
