# a = 2
# b = 15
# res = 0
# if a < b:
#     while a <= b:
#          if a % 2:
#             res += a
#     a += 1
#     print(res)
# else:
#     while b <= a:
#         if b % 2:
#             res += b
#         b += 1
#     print(res)

# a = 2
# b = 15
# res = 0
# if a > b:
#     a, b = b, a
# while a <= b:
#      if a % 2:
#          res += a
#     a += 1
#     print(res)
# else:
#     while b <= a:
#         if b % 2:
#             res += b
#         b += 1
#     print(res)

# -----------------------------------------------------------

# a = [letter *2 for letter in "Hello"]
# print(a)
#
# for i in "Hello":
#     print(i * 3, end=" ")

# ------------------------------------------------------------

# num = [i for i in range(30) if i % 2 == 0]
# print(num)
#
# print([i for range(30) if i % 2 == 0])

# ------------------------------------------------------------
# Списки (list)

# num = [8, 3, "one", 3.2, [1, 2, 3]]
# print(num)
# print(type(num))
# print(num[1])
# print(num[-1][1])
# print(num[-2])
# num[2] = 256
# print(num)
# num[1] += 100
# num [-1] = 2
# print(num)
# num[5] = 4
# print(num)
# print("Длина списка: ", len(num))
# -------------------------------------------------------------

# s = []
# print(type(s))
# b = list("Hello")
# print(b)

# -------------------------------------------------------------

# s = [5, 1] * 6
# print(s)

# -------------------------------------------------------------
# n = list(range(2, 10, 2))
# print(n)
# n2 = [2, 4, 6, 8]
# print(n2)
#
# if n is n2:
#     print("списки равны")
# else:
#     print("списки разные")
# -------------------------------------------------------------

# [выражение for переменная in последовательность]
# n = 5
# a = [i ** 2 for i in range(1, n+1)]
# print(a)

# -------------------------------------------------------------

# a = [1, 2, 3]
# b = [5, 6]
# c = a + b
# print(c)
# d = c * 2
# print(d)

# -------------------------------------------------------------
# a = [0] * int(input("Введите количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("-> "))
#     print(a)
#
# b = [0, 0, 0]
# b[0] = 5
# b[1] = 6
# b[2] = 7
# -------------------------------------------------------------
# a = [int(input("-> ")) for i in range(int(input("Кол-во эл-тов: ")))]
# print(a)
# -------------------------------------------------------------
# a = [4, 8, 9, 3, 2]
# for i in range(len(a)):
#     print(i)
#     print(a[i], end=" ")
#     print()
#     for i in a:
#         print(elem + 1, end=" ")
# -------------------------------------------------------------

# lst = ['один', 'два', 'три']
# for elem in lst:
#     print(elem, end=" ")
# print()
# for i in range(len(lst)):
#     print(lst[i] * 2, end=" ")

# ----------------------------------------------------------------

# a = [int(input('-> '))for i in range(int(input('Введите количество элементов: ')))]
# summa = 0
# for i in a:
#     summa += i if i<0 else 0
# print('Сумма отрицательных элементов:', summa)
# --------------------------------------------------------------------
# sum1 = 0
# a = [0] * int(input("Введите количество элементов списка: "))
# for i in range(len(a)):
#     a[i] = int(input("-> "))
#     if a[i] < 0:
#         sum1 += a[i]
# print(sum1)

# -----------------------------------------------------------------------
# count = 0
# lst = [int(input('=> ')) for _ in range(int(input('Введите количетсов элементов ')))]
#
# for i in lst:
#     if i < 0:
#         count += i
# print(f'сумма отрицательных элементов {count}')

# ---------------------------------------------------------------------------

# n = list(range(21, 41))
# print(n)
# k = s = 0
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         k += 1
#     else:
#         s += n[i]
# print("Количество четных элементов: ", k)
# print("Сумма нечетных элементов: ", s)

# ----------------------------------------------------------------------------
# n = 5
# zero_elem = 0
# sum = 0
# lst = [int(input('-Ю')) for _ in range(n)]
# for i in lst:
#     if i == 0:
#         zero_elem += 1
#     sum += i
# print('Среднее арифметическое - ', sum / (n - zero_elem))
# ----------------------------------------------------------------------------
# a = [int(input('-> '))for i in range(int(input('Введите количество элементов: ')))]
# count = 0
# summa = 0
# for i in a:
#     summa += i
#     count += 1 if i != 0 else 0
# print('Среднее арифметическое: ', summa/count)
# ----------------------------------------------------------------------------
# a = [int(input("->")) for i in range(int(input("Количество элементов: ")))]
# for i in range(len(a)):
#     if i % 2 == 0:
#         print(a[i],end=' ')
# ----------------------------------------------------------------------------
# a = [7, 8, 2, 1, 17]
# print(a)
#  a[0], a[-1] = a[-1], a[0]
#  print(a)
# ----------------------------------------------------------------------------
# size = int(input("Введите размер поля: ")) # homework
# symbol = int(input("Введите количество символов: "))
# for i in range(size):
#     for j in range(symbol):
#         for n in range(size):
#             for m in range(symbol):
#                 if (i * n)% 2 == 0:
#                     print("*", end="")
#                 else:
#                     print(" ", end="")
#         print()

#   print(" " if (i + n) % 2 else "*", end="") - ne nado
# ----------------------------------------------------------------------------
# Срезы
# список [start;stop;step]
# s = [5, 9, 3, 7, 1, 8]
# print(s[1:4])
# print(s[2:])
# print(s[:2])
# print(s[1::2])
# print(s[::-1])
# print(s[-2:2:-1])
# print(s[10:20])
# ----------------------------------------------------------------------------
# s = [1, 2, 3, 4, 5, 6, 7]
# print(s[:])
# print(s[::-1])
# print(s[::2])
# print(s[1::2])
# print(s[:1])
# print(s[-1:])
# print(s[3:4])
# print(s[4:])
# print(s[-3:1:-1])
# print(s[2:5])
#
# s[1:3] = [0, 0, 0, 0]
# print(s)
# s[1:2] = [20]
# print(s)
# s[3] = [30]
# print(s)
# ----------------------------------------------------------------------------
# #методы списков
# s = [1, 20, 0, 30, 4, 5, 6, 7]
# print(s)
# s.append(99) #добавляет 1 элемент в конец списка
# print(s)
# s.extend([9, 8, 7]) #добавляет множество элементов в конец списка
# print(s)
# s.extend('add')
# print(s)
# s.insert(1, 100) #добавляет заданное значение (2 параметр) по указанному индексу (1-й параметр)
# print(s)
# ----------------------------------------------------------------------------
# s = []
# for i in range(1,10):
#     s.extend([i**2])
# print(s)
# ----------------------------------------------------------------------------
# lst = []
# n = int(input("Кол-во элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     # lst.append(x)
#     # lst.extend([x])
#     lst.insert(0, x)
# print(lst)
# ----------------------------------------------------------------------------
# n = int(input('Введите количество элементов списка: '))
# i = 0
# lst = []
# while i < n:
#     x = int(input('Ввведите число кратное 3: '))
#     if x % 3 != 0:
#         print(x, 'число не делится на 3 без остатка')
#     else:
#         lst.append(x)
#     i += 1
# print(lst)
# ----------------------------------------------------------------------------
# a = [5, 9, 2, 1, 4, 3]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)
# ----------------------------------------------------------------------------
# a = [1, 2, 3, 4, 2]
# b = [11, 22, 33]
# c = []
# print("a =", a)
# print("b =", b)
# if len(b) > len(a):
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)): #range(3, 5)
#         c.append(b[i])
#
# else:
#     for i in range(len(b)):
#             c.append(b[i])
#             c.append(a[i])
#     for i in range(len(b), len(a)):
#             c.append(a[i])
# print(c)
# ----------------------------------------------------------------------------
# s = [1, 20, 0, 30, 4, 5, 6, 7, 0, 0, 2]
# s[2:] = []
# if 2 in s:
#     s.remove(20) #удаляет элемент по значению, первое совпадение
#     i += 1
# print(s)
# last = s.pop() #удаляет последний элемент из списка и возвращает удаляемый элемент
# print(last)
# print(s)
# second = s.pop(0)#удаляет элемент по индексу
# print(second)
# print(s)
# # s.clear()
# # del s[:]
# del s[2]
# print(s)
# ----------------------------------------------------------------------------
# s = []
# m = [s.append(int(input('-> '))) for i in range(int(input('Введите количество элементов: ')))]
# k = int(input('Введите индекс: '))
# del s[k]
# print(s)
# ----------------------------------------------------------------------------
# s = [1, 20, 0, 30, 4, 0, 5, 6, 7, 0, 2]
# num = s.count(0) # считает количество заданных значений в списке
# print(num)
#
# ind = s.index(0) # возврат положение первого индекса с заданным значением
# print(ind)
# ----------------------------------------------------------------------------
# a = [1, 2, 3]
# b = a
# s_copy = a.copy() #возвращает копию списка расположенную по другому адресу
# print("a =", a)
# print("b =", b)
# print("s_copy =", s_copy)
# a.append(20)
# b.append(4)
# s_copy.append(444)
# print("a =", a)
# print("b =", b)
# print("s_copy =", s_copy)
# print(id(a))
# print(id(b))
# print(id(s_copy))
# ----------------------------------------------------------------------------
# s = [1, 20, 0, 30, 4, 0, 5, 6, 7, 0, 2]
# s.reverse() #возвращает None, переставляет элементы списка в обратном порядке
# print(s)
# s.sort(reverse=True)
# print(s)
#
# s2 = ["Vitalyi", "Sergey", "Alexander", "Anna"]
# s2.sort(key=len, reverse=True)
# print(s2)
# ----------------------------------------------------------------------------
# print(dir(list))
# ----------------------------------------------------------------------------
# генерация случайных данных
import random
import time
from random import randint, randrange

# print(random.random())
# print(randint(0, 9))
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------


# m = [
#     [1, 2, 3, 4], # stroka 0
#     [5, 6, 7, 8], # stroka 1
#     [9, 10, 11, 12] #stroka 2
# ]
# print(m)
# print(m[1][2])
#
# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end='\t')
#     print()
# --------------------------------------------------------
# for row in m:
#     for x in row:
#         print(x, end='\t')
#     print()
# --------------------------------------------------------
# m = [
#     [1, 2, 3, 4], # stroka 0
#     [5, 6, 7, 8], # stroka 1
#     [9, 10, 11, 12] #stroka 2
# ]
#
# for row in m:
#     for x in row:
#         print(x**2, end='\t')
#     print()
# ------------------------------------------------------------
# n, m = int(input('Введите высоту матрицы: ')), int(input('Введите ширину матрицы: '))
# matr = [[0 for i in range(m)] for j in range(n)]
# for row in matr:
#     for x in row:
#         print(x, end='\t')
#     print()
# -----------------------------------------------------------
# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, "+", y, "=", x + y)
# -----------------------------------------------------------
# w, h = 5, 4
# matrix = [[randint(1, 30) for x in range(w)] for y in range(h)]
# for row in matrix:
#     for x in row:
#         print(x, end='\t')
#     print()
# -------------------------------------------------------------
# w, h = 3, 4
# matrix = [[randint(-20, 10) for i in range(w)] for j in range(h)]
# count = 0
# for row in matrix:
#     for x in row:
#         if x <0:
#             count +=1
#         print(x, end='\t')
#     print()
# print('Количество отрицательных элементов: ', count)
# -------------------------------------------------------------
# w, h = 6, 6  # int(input("Число значений в строке"))
# matrix = [[random.randint(0, 10) for i in range(w)] for j in range(h)]
# print(matrix)
# for i in range (0, 2, 6):
#     print(i)
#     matrix[i],matrix[i+1]=matrix[i+1],matrix[i]
# print(matrix)
# -------------------------------------------------------------
# import math
#
# print(dir(math))
# num1 = math.sqrt(2)
# print(num1)
# num2 = math.ceil(3.2)
# print(num2)
# num3 = math.floor(3.8)
# print(num3)
#
# radius = 9
# print('Площадь окружности с радиусом', radius, "=>", math.pi * radius ** 2)
# print(round(2 * math.pi * radius, 2))
# --------------------------------------------------------------------------
# import time
#
# second = time.time()
# print("Секунды с начала эпохи:", second)
# localtime = time.ctime(0)
# print(localtime)
# res = time.localtime(second)
# print(res)
# print(res.tm_year)
# print(time.strftime("Today is %B %d, %Y"))
# print(time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime(799979748)))
#
#
# pause = 5
# print("Program started...")
# time.sleep(pause)
# print(pause, "seconds.")
# --------------------------------------------------------------------------------
# test = input("Название напоминания: ")
# local_time = float(input("Через сколько минут: "))
# local_time = local_time * 60
# time.sleep(local_time)
# print(text)
# --------------------------------------------------------------------------
# import time
#
# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# res = finish - start
# print(res)
# -----------------------------------------------------------
# import locale
# locale.setlocale(locale.LC_ALL, 'ru')
#
# print(time.strftime("Сегодня: %B %d, %Y" ))
# -----------------------------------------------------------
# def hello(name):
#     print("Hello,", name, "Say", word)
#
# hello("Irina", 'hi')
# hello("Ivan", 'hello')
# ----------------------------------------------------------
# def get_sum(a, b):
#     print(a * b)
#
# x = 2
# y = 5
# get_sum(x, y)
# n = 7
# m = 9
# get_sum(n, m)
# get_sum('abc', 'def')
# ----------------------------------------------------------
# def get_sum(a, b):
#     print(a + b)
#
# x = 2
# y = 5
# res = get_sum(x, y)
# print(res)
# print("!!!", get_sum(1, 8))
# ---------------------------------------------------------
# def maximum(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
# print(maximum(9, 16))
# -----------------------------------------------------------
# def maximum(a, b):
#     if a > b:
#         return a - b
#     else:
#         return a + b
#
# a = int(input("a = "))
# b = int(input("b = "))
# print("Результат: ", maximum(a, b))

# -----------------------------------------------------------
# def change(lst):
#     # lst[0], lst[-1] = lst[-1], lst[0]
#     start = lst.pop()
#     end = lst.pop(0)
#     lst.append(end)
#     lst.insert(0, start)
#     return lst
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))
# -----------------------------------------------------------
# def is_greater(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# print(is_greater(10, 5))
# print(is_greater(5, 10))
# -----------------------------------------------------------
# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if 'A' <= ch <= '2':
#             has_upper = True
#         elif 'a' <= ch <= 'z':
#             has_lower = True
#         elif '0' <= ch <= '9':
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Это надежный пароль")
# else:
#     print("Это ненадежный пароль")
# -----------------------------------------------------------
# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# q = 2
# print(get_sum(1, 5, d=2))
# -----------------------------------------------------------
# def get_str(n=20, symbol='-'):
#     return symbol * n
#
#
# print(get_str())
# num = int(input('Введите число: '))
# sym = input('Введите символ: ')
# print(get_str(num, sym))
# -----------------------------------------------------------
# def digit_sum(n):
#     s = 0
#     while n > 0:
#         cur_digit = n % 10
#         if cur_digit % 2 == 0:
#             s += cur_digit
#         n //= 10
#     return s
#
#
# print("Сумма четных цифр: ")
# print(digit_sum(9874023))
# print(digit_sum(38271))
# print(digit_sum(123456789))
# -----------------------------------------------------------
# def digit_sum(n, even=True):
#     s = 0
#     while n > 0:
#         cur_digit = n % 10
#         if even and cur_digit % 2 == 0:
#             s += cur_digit
#         elif not even and cur_digit % 2:
#             s += cur_digit
#         n //= 10
#     return s
#
#
# print("Сумма четных цифр: ")
# print(digit_sum(9874023))
# print(digit_sum(38271))
# print(digit_sum(123456789))
# print("Сумма нечетных цифр: ")
# print(digit_sum(9874023, even=False))
# print(digit_sum(38271, even=False))
# print(digit_sum(123456789, even=False))
# -----------------------------------------------------------
# def display_info(name, age):
#     print("Name:", name, "\nAge:", age)
#
#
# display_info("Ira", 23)
# display_info(23, "Ira")
# display_info(age=23, name="Ira")
# display_info("Igor", age=23, name="Ira")
# -----------------------------------------------------------
# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(id(lt1))
# print(id(lt2))
# print(lt1 == lt2)
# print(lt1 is lt2)
#
# a = 'Hello'
# b = 'Hello'
# print(a == b)
# print(a is b)
# -----------------------------------------------------------
# lt1 = [1, 2, 3]
# print(id(lt1))
# lt1.append(4)
# print(lt1)
# lt1.pop(1)
# print(lt1)
# lt1[1] = 'Hello'
# print(lt1)
# print(id(lt1[1]))
# print(id(lt1))
# -----------------------------------------------------------
# s = "Hello"
# print(id(s))
# # s += 'World'
# s = s + 'World'
# print(s)
# print(id(s))

# -----------------------------------------------------------
# a = 5
# print(id(a))
# a += 1
# print(a)
# print(id(a))
# -----------------------------------------------------------
# s = "Hello"
# print(id(s))
# s = s[1:-1]
# print(s)
# print(id(s))
# -----------------------------------------------------------
# lt1 = [1, 2, 3]
# print(id(lt1))
# # lt1 = lt1[1:-1]
# lt1 = lt1 + [4, 5]
# print(lt1)
# print(id(lt1))
# -----------------------------------------------------------
# Кортеж

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())
# -----------------------------------------------------------
# a = (1, 2, 3, 4, 5)
# print(type(a))
# print(a)
# # b = tuple()
# # print(type(b))
#
# c = tuple("Hello")
# print(c)
# -----------------------------------------------------------
# b = tuple((1, 2, 3, 4, 5))
# print(b)
#
# print(b[3])
# print(b[1:3])
#
# b[1] = 3
# -----------------------------------------------------------
# s = tuple(int(input("-> ")) for i in range(3))
# print(s)
#
# s = input("Строка: ")
# a = tuple(s)
# print(a)

# mas = [randint(0, 100) for i in range(10)]
# print(mas)
# tpl = tuple(mas)
# print(tpl)
#
# print(tuple(randint(0, 100) for _ in range(10)))
# # -----------------------------------------------------------
# print(tuple(2 ** i for i in range(1, 13)))
# # -----------------------------------------------------------
# t1 = tuple('Hello')
# t2 = tuple('world')
#
# t3 = t1 + t2
# print(t3)
# print(len(t3))
# print(t3.count('l'))
# print(t3.count('a'))
# print(t3.index('a'))
# print(t3.index('l', 4))
# for i in t3:
#     print(i, end=' ')

# -----------------------------------------------------------
# lst = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8, ],
#     [9, 10, 11, 12]
# ]
# row = 0
# for row in lst:
#     for col in row:
#         print(col, end='\t')
#     print()
# print("--------------------")
# print(row)
# print("--------------------")
# i = 0
# for col in row:
#     print("*" * 5)
#     print(col)
#     print("*" * 5)
# for row in lst:
#         print("=" * 5)
#         print(row)
#         print("=" * 5)
#         print(row[i], end='\t')
#     i += 1
#     print()
# -----------------------------------------------------------
# def ran(a, b):
#     return tuple(randint(a,b) for _ in range(10))
#
# tpl1 = ran(0, 6)
# tpl2 = ran(-5, 1)
# print(tpl1)
# print(tpl2)
# tpl3 = tpl1 + tpl2
# print(tpl3)
# print('0 =', tpl3.count(0))
# -----------------------------------------------------------
# a = 123456
# s = str(a)
# lst = list(s)
# print(lst)
# lst1 = []
# for i in lst:
#     lst1.append(int(i))
# print(''.join(lst))
# -----------------------------------------------------------
# t = (10, 11 [1, 2, 3], (4, 5, 6), ['hello', 'world'])
# print(t, id(t))
# print(id(t[4]))
# t[-1][0] = 'new'
# t[4].append('hi')
# print(id(t[4]))
# print(t, id(t))
# -----------------------------------------------------------
# def create_tuple(lst):
#     s = []
#     for i in lst[::-1]:
#         if i not in s:
#             s.append(i)
#     return tuple(s)
#
# print(create_tuple([1, 2, 3, 3, 2]))
# print(create_tuple([2, 1, 3, 1, 2, 5, 5, 9, 2, 0, 0]))
# -----------------------------------------------------------
#lambda-выражения, анонимные функции

# (lambda x, y: print("res =", x == y))(1, 2))
# print("res =", (lambda x, y: x + y)('a', 'b'))
#
# func = (lambda x, y: x + y)
# print(func(1, 2))
# print(func('a', 'b'))
# -----------------------------------------------------------
# summ = lambda a = 1, b = 2, c = 3: a + b + c
#
# print(summ())
# print(summ(10))
# print(summ(10, 20))
# -----------------------------------------------------------
# func1 = lambda *args: args
#
# print(func1(1, 2, 3, 4))
# print(func1('a', 'b'))
# -----------------------------------------------------------
# c = (lambda x: x * 2,
#      lambda x: x * 3,
#      lambda x: x * 4)
#
# for t in c:
#     print(t("abc_"))
# -----------------------------------------------------------

# def inc1(n):
#     def wrap(x):
#         return x + n
#
#     return wrap
#
#
# f1 = inc1(42)
# print(f1(3))
#
#
# def inc(n):
#     return lambda x: x + n
#
#
# f = inc(42)
# print(f(3))
# inc2 = (lambda n: (lambda x: x + n))
# # f2 = inc2(42)
# # print(f2(3))
# print(inc2(42)(3))
#
# print((lambda n: (lambda x: x + n))(42)(3))
#

# -----------------------------------------------------------
# print((lambda a: (lambda b: (lambda c: a + b + c)))(2)(4)(6))
# -----------------------------------------------------------
# def func(i):
#     return i[1]
#
#
# d = {'b': 15, 'a': 10, 'c': 24}
# lst = list(d.items())
# print(lst)
# # lst.sort(key=lambda i: i[1], reverse=True)
# lst.sort(key=func(), reverse=True)
# print(lst)
# dict1 = dict(lst)
# print(dict1)
# -----------------------------------------------------------
# players = [{'name': 'Антон', 'last name': 'Бирюков', 'raiting': 9},
#           {'name': 'Алексей', 'last name': 'Бодня', 'raiting': 10},
#           {'name': 'Федор', 'last name': 'Сидоров', 'raiting': 4},
#           {'name': 'Михаил', 'last name': 'Семенов', 'raiting': 6}]
#
# players1 = ['Наталья', 'Виктор', 'Саша']
#
# players1.sort(key=len)
# print(players1)
#
# res = sorted(players, key=lambda item: item['last name'])
# print(res)
# players.sort(key=lambda item: item['last name'])
# print(players)
# res = sorted(players, key=lambda item: item['raiting'])
# print(res)
# res = sorted(players, key=lambda item: item['raiting'], reverse=True)
# print(res)
# -----------------------------------------------------------
# a = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x * y), (lambda x, y: x / y)]
# b = a[2](12, 5)
# print(b)
# -----------------------------------------------------------
# a = {'one': lambda x: x-1, 'two': lambda x: abs(x) - 1, 'three': lambda x: x}
# b = [-3, 10, 0, 2]
# for i in b:
#     if i < 0:
#         print(a['two'](i))
#     elif i > 0:
#         print(a['one'](i))
#     else:
#         print(a['three'](i))
# -----------------------------------------------------------
# d = {
#     1: (lambda: print('Понедельник')),
#     2: (lambda: print('Вторник')),
#     3: (lambda: print('Среда')),
#     4: (lambda: print('Четверг')),
#     5: (lambda: print('Пятница')),
#     6: (lambda: print('Суббота')),
#     7: (lambda: print('Воскресенье')),
# }
#
# d[5]()
# -----------------------------------------------------------
# maximum = (lambda a, b: a if a > b else b)
# print(maximum(15, 23))
#
# minimum = (lambda a, b, c: a if (a < b and a < c) else (b if b < a and b < c else c)
# print(minimum(11, 2, 5)
# -----------------------------------------------------------
# Функция map()
#
# def multiple(t):
#     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
#
# print(list(map(multiple, lst)))
# print(list(map(lambda t: t * 2, range(2, 10))))
# -----------------------------------------------------------
# t = (2.88, -1.75, 100.55)
#
# print(list(map(lambda x: str(x), t)))
#
#
# a = ['2.88', '-1.75', '100.55']
# b = list(map(float, a))
# print(b)
# print(list(int, map(float, a)))
# -----------------------------------------------------------
# areas = [3.578945, 5.789456, 7.456789, 56.4123456, 9.0123456, 32.7789456]
# print(list(map(round, areas, (2, 6, 4, 3))))

# -----------------------------------------------------------
# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
#
# lst = list(map(lambda x, y: [x, y], st, num))
# print(lst)
# tp = dict(lst)
# print(tp)
# -----------------------------------------------------------
# 11 == [1, 2, 3]
# 12 == [4, 5, 6]
#
# print(list(map(lambda x, y: x + y, 11, 12)))
# -----------------------------------------------------------
# -----------------------------------------------------------
# -----------------------------------------------------------
# Функция filter(func, iterable)

# t = ('abcd', 'abc', 'cdefg', 'def', 'ghi')
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)
#
# b = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# res = list(filter(lambda s: 75 < s < 88, b))
# print(res)
# -----------------------------------------------------------
# from random import *
# lst = [randint(1, 40) for i in range(10)]
# print(lst)
# res = list(filter(lambda s: 10 <= s <= 20, lst))
# print(res)
# -----------------------------------------------------------
# lst = [45, 55, 60, 37, 100, 105, 220]
# res = list(filter(lambda s: s % 15 == 0, lst))
# print(res)
# -----------------------------------------------------------
#------------------------------Декораторы------------------------------

# def hello():
#     return "Hello, I am func 'hello'"
#
#
# def super_func(func):
#     print("hello, I am func 'super_func'")
#     print(func())
#
#
# super_func(hello)
#
# test = hello
# print(test())
# -----------------------------------------------------------
# def my_decorator(func):
#     def wrap():
#         print('Code before')
#         func()
#         print('Code after')
#     return wrap
#
#
# def func_test():
#     print("Hello, I am func 'func_test'")
#
#
# test = my_decorator(func_test)
# test()
# -----------------------------------------------------------
# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
#
# @bold
# @italic
# def hello():
#     return "text"
#
#
# print(hello())
# -----------------------------------------------------------
# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print("Вызов функции: ", count)
#
#     return wrap
#
# @cnt
# def hello():
#     print("Hello")
#
#
# @cnt
# def bye():
#     print("Good bye")
#
#
# hello()
# hello()
# bye()
# hello()
#
# bye()
#
# bye()
# bye()
# -----------------------------------------------------------
# def args_decorator(fn):
#     def wrap(arg1, arg2):
#         print("*" * 50)
#         fn(arg1, arg2)
#         print("*" * 50)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#
#
# print_full_name("Ирина", "Лаврова")
# -----------------------------------------------------------
# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         fn(*args, **kwargs)
#         print("*" * 50)
#         print("args:", args)
#         print("kwargs:", kwargs)
#         print("*" * 50)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(a, b, c, study='Python'):
#     print(a, b, c, "изучают", study, end="\n\n")
#
#
# print_full_name("Ирина", "Борис", "Светлана", study='JavaScript')
# print()
# print_full_name("Владимир", "Екатерина", "Виктор")
# -----------------------------------------------------------
# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(*x):
#             print("args1", x[0], args2, x[1], "=", end=" ")
#             fn(*x)
#
#         return wrap
#
#     return
#
#
# @decor("Сумма:", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность:", "-")
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)
# -----------------------------------------------------------
# def multiply(n):
#     def return_mult(fn):
#         def wrap(num):
#             return 'Результат: ', + str(fn(num) * n)
#         return wrap
#
#     return return_mult
#
#
# @multiply(3)
# def return_num(num):
#     return num
#
#
# print(*return_num(5))
# -----------------------------------------------------------
def typed(*args, **kwargs):
    def wrapper(fn):
        def wrap(*f_args, **f_kwargs):
            for i in range(len(args)):
                if type(f_args[i]) != args[i]:
                    raise TypeError("Некорректный тип данных")
            return fn(*f_args, **f_kwargs)
        return wrap
    return wrapper


@typed(int, int, int)
def typed_fn(x, y, z):
    return x * y * z


def typed_fn2(x, y, z):
    return x + y + z


def typed_fn3(x, y, z="Hello! "):
    return (x + y) * z


print(typed_fn(3, 4, 5))
print(typed_fn(3, 4, "Doge"))
print(typed_fn2("Hello, ", "World", "!"))
print(typed_fn3("Hello, ", "World", z=5))
# -----------------------------------------------------------

# -----------------------------------------------------------

# -----------------------------------------------------------

# -----------------------------------------------------------

# -----------------------------------------------------------

# -----------------------------------------------------------

# -----------------------------------------------------------

# -----------------------------------------------------------

# -----------------------------------------------------------

# -----------------------------------------------------------

# -----------------------------------------------------------

# -----------------------------------------------------------

# -----------------------------------------------------------

# -----------------------------------------------------------

# -----------------------------------------------------------

# -----------------------------------------------------------

# -----------------------------------------------------------

# -----------------------------------------------------------

# -----------------------------------------------------------

# -----------------------------------------------------------





























































#------------------------------------------------------------------------------
# from random import *
#
# def get_count(numbers):
#     count = 0
#     for i in numbers:
#         if i > 0 and i % 13 == 0 and i > count:
#             count = i
#     return count if count > 0 else 'no such numbers'
#
# print('Примеры из задания:')
# print(get_count([2, 7, 0, 3, 1, 5]))
# print(get_count([2, 7, 0, 3, 1, 5, -13, 13]))
# print(get_count([26]))
# print(get_count([99, 99, 100, 34, -39]))
# print(get_count([99, 39, 99, 100, 34]))
# print('Рандомный список:')
# random_list = [randint(-1000, 1001) for _ in range(randint(1, 100))]
# print(random_list)
# print(get_count(random_list))
# print('Проверим ваш список! Введите число по одному, если хотите остановиться: введите 0')
# lst = []
# while True:
#     n = int(input('->'))
#     lst.append(n)
#     if n == 0:
#         break
# print('Ваш список:', lst)
# print('Наибольшее положительное число, кратное 13 из вашего списка:', end=' ')
# print(get_count(lst))
#------------------------------------------------------------------------------
# print("Задание 1")
#
# def s_input():  # ВАРИАНТ
#     l = []
#     for i in set(input("Запишите через запятую в строку целые числа.").split(",")):
#         l.append(int(i))
#     l.sort()
#     return tuple(l)
#
# def s_input2():
#     l = []
#     b, d = 0, 1
#     c = list(input("Запишите через запятую в строку целые числа."))
#     for i in c:
#         if i == '-':
#             d *= -1
#             continue
#         try:
#             b = b * 10 + int(i)
#         except ValueError:
#             l.append(b * d)
#             b, d = 0, 1
#     l.append(b)
#     l.sort()
#     l = set(l)
#     print(l)
#     return tuple(l)
#
# def l13_max(sett: set):
#     smax = False
#     for i in sett:
#         smax = (i if i > smax and i % 13 == 0 and i > 0 else smax)
#     if smax == False:
#         smax = "NO NUMS"
#     return (smax)
#
# print(l13_max(s_input2()))
# print()
# print()
# print('Задание 2')
# print()
# s = input("Введите искомый элемент")
# t = ('ab', 'abcd', 'cde', 'def')
# print("Исходный кортеж", t)
# if s in t:
#     print("Yes")
# else:
#     print("No")
# print()
# print()
# print("Задание 3")
# print()
# str = input('Введите по порядку, без пробелов,элементы кортежа')
#
# def str_to_spis(strr):
#     a = list(strr)
#     a1, a2 = [], []  # Знак и количество
#     for i in a:
#         if i in a1:
#             for j in range(len(a1)):
#                 if a1[j] == i:
#                     a2[j] += 1
#
#         else:
#             a1.append(i)
#             a2.append(1)
#     return (a1, a2)
#
# def print_spis(bb):
#     bb1, bb2 = bb
#     print("Статистика частотности символов")
#     for i in range(len(bb1)):
#         print("Количество ", bb1[i], " = ", bb2[i])
#
# print_spis(str_to_spis(str))
#------------------------------------------------------------------------------
