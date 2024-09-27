import math


class Figure:
    sides_count = 0

    def __init__(self, color=(0, 0, 0), *sides):
        if len(sides) != self.sides_count:
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = list(sides)
        self.__color = list(color)
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        for i in (r, g, b):
            if not isinstance(i, int) or not (0 <= i <= 255):
                return False
            else:
                return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            print("Некорректные значения для цвета!")

    def get_sides(self):
        return self.__sides

    def __is_valid_sides(self, *new_sides):
        if len(new_sides) != self.sides_count:
            return False
        for s in new_sides:
            if not (isinstance(s, int) and s > 0):
                return False
        else:
            return True

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
        else:
            print("Некорректные значения сторон или неправильное количество.")

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color=(0, 0, 0), circumference=1):
        super().__init__(color, circumference)
        self.__radius = circumference / (2 * 3.14159)

    def get_square(self):
        return math.pi * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__(color, *sides)

    def get_square(self):
        s = len(self) / 2
        a, b, c = self.get_sides()
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color=(0, 0, 0), edge_length=1):
        super().__init__(color)
        self.set_sides(*[edge_length] * self.sides_count)

    def get_volume(self):
        return self._Figure__sides[0] ** 3

    def set_edge_length(self, edge_length):
        if isinstance(edge_length, (int, float)) and edge_length > 0:
            self.set_sides(*[edge_length] * self.sides_count)
        else:
            print("Некорректная длина ребра.")


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
