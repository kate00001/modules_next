class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}.")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}.")
            self.alive = False


class Plant:
    edible = False

    def __init__(self, name):
        self.name = name


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Flower(Plant):
    pass


class Fruit(Plant):
    edible = True


dog = Predator('Собакен')
horse = Mammal('Лошадка')
orange = Fruit('Апельсинка')
clover = Flower('Клевер-четырехлистник')

dog.eat(orange)
dog.eat(clover)
horse.eat(orange)

print(f'Жив ли наш собакен? - {dog.alive}')
print(f'Накормлена ли лошадка? - {horse.fed}')
print(f'А жива? - {horse.alive}')
