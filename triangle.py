class PositiveInteger:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Значение должно быть положительным целым числом")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class Triangle:
    a = PositiveInteger()
    b = PositiveInteger()
    c = PositiveInteger()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_exist(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            return True
        else:
            return False


triangle1 = Triangle(2, 5, 6)
if triangle1.is_exist():
    print("Треугольник со сторонами ({}, {}, {}) существует.".format(triangle1.a, triangle1.b, triangle1.c))
else:
    print("Треугольник со сторонами ({}, {}, {}) не существует.".format(triangle1.a, triangle1.b, triangle1.c))

triangle2 = Triangle(5, 2, 8)
if triangle2.is_exist():
    print("Треугольник со сторонами ({}, {}, {}) существует.".format(triangle2.a, triangle2.b, triangle2.c))
else:
    print("Треугольник со сторонами ({}, {}, {}) не существует.".format(triangle2.a, triangle2.b, triangle2.c))

triangle3 = Triangle(7, 3, 6)
if triangle3.is_exist():
    print("Треугольник со сторонами ({}, {}, {}) существует.".format(triangle3.a, triangle3.b, triangle3.c))
else:
    print("Треугольник со сторонами ({}, {}, {}) не существует.".format(triangle3.a, triangle3.b, triangle3.c))