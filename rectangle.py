def init(self, length, width):


    self.length = length
    self.width = width


def area(self):
    return self.length * self.width


def perimeter(self):
    return 2 * (self.length + self.width)


def diagonal(self):
    return (self.length ** 2 + self.width ** 2) ** 0.5


def draw(self):
    for i in range(self.width):
        print("*" * self.length)


    rect = Rectangle(3, 9)
    print("Длина прямоугольника:", rect.length)
    print("Ширина прямоугольника:", rect.width)
    print("Площадь прямоугольника:", rect.area())
    print("Периметр прямоугольника:", rect.perimeter())
    print("Гипотенуза прямоугольника:", rect.diagonal())
    print("Прямоугольник:")
    rect.draw()
