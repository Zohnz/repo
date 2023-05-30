# # Декораторы продолжение
# def decor(tx=None, decor_text=''):
#     def wrapper(fn):
#         def wrap(*args):
#             print(decor_text, end="")
#             fn(*args)
#
#         return wrap
#
#     if tx is None:
#         return wrapper
#     else:
#         return wrapper(tx)
#
#
# @decor
# def hello_world2(text):
#     print(text)
#
#
# @decor(decor_text="Hello, ")
# def hello_world(text):
#     print(text)
#
#
# hello_world2("Hi!")
# hello_world("world!")

#Символы
# ---------------------------------------------------------------------
# print(int('100', 2))
# print(int('100', 8))
# print(int('100', 16))
# print(int('100', 10))
# print(int('100', 32))
# ---------------------------------------------------------------------
# print(bin(18)) # 0b10010  # 0B
# print(oct(18)) # 0o22     # 0O
# print(hex(18)) # 0x12     # 0X

#---------------------------------------------------------------------

# print(0b100 + 2)
# print(0o20 + 4)
# print(0x11 + 3)

#---------------------------------------------------------------------

# def change_char(s, c_old, c_new):
#     s2 = ""
#     for i in s:
#         if i == c_old:
#             i = c_new
#         s2 += i
#     return s2
#
#
# st = 'Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования'
# st2 = change_char(st, 'N', 'P')
# print('st1 = ', st)
# print('st2 = ', st2)
#---------------------------------------------------------------------
#
# print(u"Привет")
# print(r'C:\file.txt') # "сырые" строки
# print('C:\\file.txt')
# print(r'C:\file.txt\\'[:-1])
# print(r'C:\file.txt' + "\\")
# print('C:\\file.txt\\')
#---------------------------------------------------------------------
# name = "Дмитрий"
# age = 25
# print("Меня зовут " + name + ". Мне ", age, " лет", sep="")
# print("Меня зовут " + name + ". Мне " + str(age) + " лет")
# print(f"Меня зовут {name}. Мне {age} лет")
#
# print({f"{round(2.356789, 2)}"})
# print(f"{2.356789:.2f}")
#---------------------------------------------------------------------

# x = 10
# y = 5
# print(f"{x} x {y} / 2 = {x * y / 2}"
#       f" - выражение")
#---------------------------------------------------------------------
# d = 74
# print(f"{{{{{d}}}}}")
#---------------------------------------------------------------------
# dir_name = 'doc'
# file_name = 'data.txt'
# print(fr'home\{dir_name}\{file_name}')
# print("home\\" + dir_name + "\\" + file_name)
#
# print(s)
#---------------------------------------------------------------------
# s1 = '''<div>
#     <a href = "#">content</a>
# </div>
# '''
# print(s1)
# s = """<div>
#     <a href = "#">content</a>
# </div>
# """
# print(s)
#---------------------------------------------------------------------
# def square(n):
#     """Принимает число n, возращает квадрат числа n"""
#     a = 5
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)
#---------------------------------------------------------------------
# import math
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * math.pi * r * (r + h)
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)
#
# doc = 5
# print(doc)