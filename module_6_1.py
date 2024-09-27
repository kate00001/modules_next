class Animal:
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
    def __init__(self, name):
        self.name = name


class Mammal(Animal):
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False


class Predator(Animal):
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False


class Flower(Plant):
    def __init__(self, name):
        self.name = name
        self.edible = False


class Fruit(Plant):
    def __init__(self, name):
        self.name = name
        self.edible = True


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
