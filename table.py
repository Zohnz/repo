import math

class Table:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

class RectangleTable(Table):
    def area(self):
        return self._width * self._length

class CircleTable(Table):
    def area(self):
        return math.pi * self._radius ** 2

rect_table = RectangleTable(_width=20, _length=10)
print(rect_table.__dict__)
print(rect_table.area())

rect_table._length = 20
print(rect_table.__dict__)
print(rect_table.area())

circ_table = CircleTable(_radius=20)
print(circ_table.__dict__)
print(circ_table.area())