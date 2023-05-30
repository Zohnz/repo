class Counting:
    __count = 0

    @staticmethod
    def triangle(a, b, c):
        p = (a + b + c) * 0.5
        s = p * (p - a) * (p - b) * (p - c)
        Counting.__count += 1
        return print("Площадь треугольника по формуле Герона", (a, b, c), ':', round((s ** (1 / 2)), 3))

    @staticmethod
    def triangle2(d, h):
        s1 = d * h * 0.5
        Counting.__count += 1
        return print('Площадь треугольника по высоте и основанию', (d, h), ":", s1)

    @staticmethod
    def rectangle(dl, h):
        s2 = dl * h
        Counting.__count += 1
        return print("Площадь прямоугольника со сторонами", (dl, h), ":", s2)

    @staticmethod
    def square(r):
        Counting.__count += 1
        return print("Площадь квадрата со стороной", r, ":", r ** 2)

    @staticmethod
    def quantity():
        return print("Количество подсчетов площади:", Counting.__count)


Counting.triangle(3, 4, 5)
Counting.triangle2(7, 6)
Counting.rectangle(2, 6)
Counting.square(6)
Counting.quantity()