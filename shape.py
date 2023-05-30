class Shape(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    def info(self):
        print(f"Фигура: {type(self).__name__}")
        print(f"Периметр: {self.perimeter()}")
        print(f"Площадь: {self.area()}")
        self.draw()


class Square(Shape):
    def __init__(self, side, color):
        self.side = side
        self.color = color

    def perimeter(self):
        return 4 * self.side

    def area(self):
        return self.side ** 2

    def draw(self):
        print("*" * self.side)
        for i in range(self.side - 2):
            print("*" + " " * (self.side - 2) + "*")
        print("*" * self.side)

    def info(self):
        super().info()
        print(f"Цвет: {self.color}")


class Rectangle(Shape):
    def __init__(self, length, width, color):
        self.length = length
        self.width = width
        self.color = color

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def draw(self):
        print("*" * self.width)
        for i in range(self.length - 2):
            print("*" + " " * (self.width - 2) + "*")
        print("*" * self.width)

    def info(self):
        super().info()
        print(f"Цвет: {self.color}")


class Triangle(Shape):
    def __init__(self, side1, side2, side3, color):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.color = color

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def area(self):
        p = (self.side1 + self.side2 + self.side3) / 2
        return round(math.sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side3)), 2)

    def draw(self):
        print(" " * (self.side1 - 1) + "*")
        for i in range(self.side2 - 1):
            print(" " * (self.side1 - i - 2) + "*" + " " * (i * 2 + 1) + "*")
        print("*" * (self.side3 * 2 - 1))

    def info(self):
        super().info()
        print(f"Цвет: {self.color}")


square1 = Square(3, "красный")
square2 = Square(3, "зеленый")
rectangle = Rectangle(7, 3, "зеленый")
triangle = Triangle(11, 6, 6, "желтый")

square1.info()
square2.info()
rectangle.info()
triangle.info()