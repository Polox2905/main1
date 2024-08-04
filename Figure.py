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
        if len(self.__sides) != self.sides_count:
           return [1] * self.sides_count
        else:
            return self.__sides

    def __len__(self):
        raise NotImplementedError("Perimeter must be implemented by subclass")

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)



class Circle(Figure):
    sides_count = 1

    def __init__(self, __color=(0, 0, 0), *args):
        super().__init__(__color, *args)
        self.side=sum(args)
        self.radius = int(*args) / (2 * math.pi)

    def get_square(self):
        return self.radius ** 2 * math.pi

    def __len__(self):
        # Длина окружности
        return int(self.side)



circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)


# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())


# Проверка на изменение сторон:
print(circle1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
