# Task 1 --------------------------------------------------
# a = [int(input('-> ')) for i in range(int(input('Введите длину списка: ')))]
# print("Список :", a)
# newlist = [n for n in a if n > 0]
#
# print("Новый список, состоящий только из положительных элементов :", newlist)
# print("Наибольший элемент списка :", (max(a)))
# Task 2 --------------------------------------------------

a = [int(input('-> ')) for i in range(int(input('Введите элементы списка: \nn = ')))]
k = int(input("Введите индекс: \nk = "))
c = int(input("Введите значение: \nc = "))
a.insert(k, c)
print(a)
# Task 3 --------------------------------------------------
# a = [int(input('-> ')) for i in range(int(input('Введите элементы списка: \nn = ')))]
# ch = int(input("Введите число: \nch = "))
# if ch in a:
#     print("Число есть в списке")
# else:
#     print("Число не входит в список")
