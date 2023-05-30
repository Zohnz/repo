# print("Hello World!")
#
# age = 20
# name = "Elena"
#
# print("Hellow,", name)
# print(age)
# print(type(name))
# print(type(age ))

# a = 4
# b = 5
# print(id(a))
# print(id(b))
#
# a = b = c = 1
# print(a, b, c)

# a = 1
# b = 2
# print("a:", a)
# print("b:", b)
# # c = a
# # a = b
# # b = c
# a, b = b, a


# day = int(input("Введите день недели (цифрой): "))
# if 1 <= day <= 5:
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("Понедельник")
#
# elif day == 6 or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("Суббота")
# else:
#     print("Такого дня недели не существует!")


# n = int(input("Введите количество ворон: "))
# if В <= n <= 9:
#     print("На ветке", end="")
#     if n == 1:
#         print(n, "ворона")
#     if 2 <= n <= 4:
#         print(n, "вороны")
#         if 5 <= n <= 9 or n == 8
#             print(n, "ворон")
# else:
#     print("Ошибка ввода данных")

# a = int(input("Введите число от 1 до 99: "))
# kop = a
# if 11 <= a <= 14:
#     print(a, "копеек")
# else:
#     kop = kop % 10
#     if kop == 1:
#         print(a, "копейка")
#     elif 2 <= kop <= 4:
#         print(a, "копейки")
#     else:
#         print(a, "копеек")


# Тернарное выражение

# a, b = 10, 20
# minim = a if a < b else b
# print(minim)
#
# a, b = 30, 30
# print("a == b" if a == b else "a > b" if a > b else "b > a")
#
# if a == b:
#     print("a == b")
# else:
#     if a > b:
#         print("a > b")
#     else:
#         print("b > a")

# Исключения

# a = 5
# b = 0
# print(a / b)
# print("Код далее")

# try:
# n = int(input("Введите целое число: "))
# print(n = 2)
# except ValueError:
# print("Что-то пошло не так")
#
# print("Код далее")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Нельзя вводить строки")
#     print("Нельзя делить на ноль")
# else:
#     print("Все нормально. Вы ввели числа", n, "и", m)
# finally:
#     print("Конец программы")


# a = int(input("Введите первое число"))
# b = int(input("Введите второе число"))
#
# for num in range (a, b + 1):
#     if num % 2! == 0:
#         print(num, b = " ")

# n = input("Введите целое число: ")
#
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число: ")
#
# if n % 2 == 0:
#     print("Чётное")
# else:
#     print("Нечетное")


# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
#     print("\nЦикл завершен!")

# while True:
#     n = int(input("Введите положительное число: "))
#     if n > 0:
#         break

# n = int(input('Введите любое число: '))
# count = 1
# while n != 0:
#     count *= n
#     n = int(input('Введите любое число: '))
# print('Произведение чисел:', count)

# sum1 = 1
# while True:
#     n = int(input('введите число '))
#     if n == 0:
#         break
#     sum1 *= n
# print(sum1)


# i = 0
# while i < 3:
#     a = 8 + i
#     i += 1
#
# print(a)


# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i =", i)

# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВложенный цикл: j =", j)
#         j += 1
#     i += 1

# i = 1
# while i <= 9:
#     j = 1
#     while j <= 9:
#         print(i, "*", j, "=", i*j, end="\t\t")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 3:
#     j = 0
#     while j < 6:
#         print('^', end='')
#         j += 1
#     print()
#     i += 1

# i = 1
# while i <= 5:
#     j=0
#     while j<20:
#         if i%2!=0:
#             print('+', end='')
#         else:
#             print('-', end='')
#         j+=1
#     print()
#     i+=1

# for element in collection:
#     print(element)

# for i in 'Hello!':
#     print(i)

# i = 0
# for color in 'red', 'orange', 'yellow', 2, 0.3:
#     print(i, "color:", color, type(color))
#     i += 1

# for i in range(n):
#     Тело цикла

# range(start, stop, step)

# for i in range(9, 0):
#     print(i, end=" ")

    # print()
    # j = 0
    # while j < 9:
    #     print(j, end=" ")
    #     j += 1


# a = int(input("Введите целое число: "))
# for i in range(1, a + 1):
#         if a % i == 0:
#             print(i, end=' ')


# for i in range(10, 100):
#     if i // 10 == i % 10:
#         print(i, end=" ")

# for i in range(10, 100):
#     if i % 11 == 0:
#         print(i, end=" ")

# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print('done')


# for i in range(3):
#     print("+++")
#     for j in range(2):
#         print("-----")


# n = int(input('введите длину '))
# m = int(input('введите высоту '))
# for i in range(m):
#     for j in range(n):
#         print('*',end='')
#     print()

# a = int(input("высота прямоугольника"))
# b = int(input("Ширина прямоугольника"))
# for i in range(a):
#     print()
#     for j in range(b):
#         if 0 < i < a - 1 \
#                 and 0 < j < b - 1:
#             print(" ", end="")
#         else:
#             print("*", end="")

# a = int(input("высота прямоугольника"))
# b = int(input("Ширина прямоугольника"))
# for i in range(a):
#     for j in range(b):
#         if i == 0 or j == 0 or i == a - 1 or j == b - 1:
#             print("*", end="")
#         # else:
#         #     print(" ", end="")
#         print()