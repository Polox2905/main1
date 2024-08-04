import math


class Figure:
    sides_count = 0
    filled = False
    __sides = []

    def __init__(self, __color=(0, 0, 0), *args):
        self.__sides = [*args]
        self.__color = __color


    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(0 <= c <= 255 for c in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, *__sides):
        return len(__sides) == self.sides_count and all(
            0 < side and isinstance(side, int) for side in __sides)

    def get_sides(self):
        if len(self.__sides) != self.sides_count and len(self.__sides) > 1:
           return [1] * self.sides_count
        elif len(self.__sides) != self.sides_count and len(self.__sides) == 1:
            return self.__sides * self.sides_count
        else:
            return self.__sides

    def __len__(self):
        raise NotImplementedError("Perimeter must be implemented by subclass")

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)



class Circle(Figure):
    sides_count = 1

    def __init__(self, __color=(0, 0, 0), __sides=[]):
        super().__init__(__color, __sides)
        self.side = __sides
        self.radius = self.side / (2 * math.pi)

    def get_square(self):
        return self.radius ** 2 * math.pi

    def __len__(self):
        # Длина окружности
        return self.side


class Cube(Figure):
    sides_count = 12

    def __init__(self, __color=(0, 0, 0), __sides=[]):
        super().__init__(__color, __sides)
        self.side = __sides

    def get_volume(self):
        return self.side ** 3

    def __len__(self):
        # Периметр куба
        return 12 * self.side



class Triangle(Figure):
    sides_count = 3

    def __init__(self, __color=(0, 0, 0), __sides=[]):
        super().__init__(__color, __sides)
        self.side1 = __sides
        self.side2 = __sides
        self.side3 = __sides


    def get_square(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def __len__(self):
        return self.side1 + self.side2 + self.side3



circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())





















