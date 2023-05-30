# class Point:
#     __slots__ = ["__x", "__y", "z"]
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x  # _Point__x
#             self.__y = y
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#     def set_coord(self, x, y):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#     def set_coord_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Координаты должны быть числами")
#     def set_coord_y(self, y):
#         if Point.__check_value(y):
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#     def get_coord(self):
#         return self.__x, self.__y
#     def get_coord_x(self):
#         return self.__x
#     def get_coord_y(self):
#         return self.__y
#
# p1 = Point(5, 10)
# p1.z = 15
# print(p1.z)
# print(p1.__dict__)
# print(p1._Point__x)
# p1._Point__x = 111
# print(p1.get_coord())
# p1.set_coord(1, 2.3)
# print(p1.get_coord())
# print(p1.__dict__)
# p1.set_coord_x(8)
# print(p1.get_coord_x())
# p1.set_coord_y(9)
# print(p1.get_coord_y())
# # p1.__x = 100
# # p1.__y = 'abc'
# # print(p1.__x, p1.__y)
# print(p1.__dict

class Point:
    def __init__(self x=0, ):
        self.__x = x
        self.__y = y

    def __set_x(self, x):
        print("Вызов __set_x")
        self.__x = x

    def __get_x(self, x):
        print("Вызов __get_x")
        return self.__x

    x = property(__get_x, __set_x)


p1 = Point(5, 10)
p1.x = 100










































