# s = ['one', 'two']
# print(s[0])
# d = {"1": 'one', 2: 'two', 1: "one"}
# print(d["1"])
#---------------------------------------------------------
# d = {'one': 1, 'two': 2}  #dict - словарь
# print(d)
# print(type(d))
#
# d1 = dict(one=1, two=2)
# print(d1)
# print(type(d1))
#---------------------------------------------------------
# a = [
#     ('igor@gmail.com', 'igor'),
#     ('irina@gmail.com', 'irina'),
#     ('anna@gmail.com', 'anna')
# ]
# d = dict(a)
# print(d)
#---------------------------------------------------------
# d = {a: a ** 2 for a in range(1, 7)}
# print(d)
# print(d[2])
# d[2] = 15
# print(d)
# d[6] = 4 ** 2
# print(d)
#---------------------------------------------------------
# d = {0: 'text', "one": 45, (1, 2.3): "кортеж", 42: [2, 3, 6, 7], True: 1 }
# print(d)
# # print(d[True])
# # print(d[(1, 2.3)])
# # print(d[42][1])
# # print('one' in d)
# # print('two' in d)
# #
# # print(d.keys())
# # if 'one' in d:
# #     print("TRUE")
# # if 'one' in d.keys():
# #     print("TRUE")
#
# # key = 2
#
# # if key in d:
# #     del d[key]
# # try:
# #     del d[key]
# # except KeyError:
# #     print("Элемента с ключом" + key + "нет в словаре")
# #
# # print(d)
# # for key in range(len(d)):
# #     print(key, "->", d[key])
#
# #---------------------------------------------------------
# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# pro = 1
# for item in d:
#     pro *= d[item]
# print(pro)
# #---------------------------------------------------------
# d = dict()
# d[1] = input("->")
# d[2] = input("->")
# d[3] = input("->")
# d[4] = input("->")
# print(d)
#
# d = {a: input("->") for a in range(1,5)}
# print(d)
# a = int(input('Какой элемент исключить? '))
# if a in d:
#     del d[a]
#     print(d)
# else:
#     print('Такого элемента нет')
# #---------------------------------------------------------
# capitals = dict()
# capitals['Russia'] = 'Moscow'
# capitals['Italy'] = 'Rome'
# capitals['Spain'] = 'Madrid'
#
# countries = ['Russia', 'Italy', 'France', 'Spain']
#
# for country in countries:
#     if country in capitals:
#         print('Столица страны ' + country + ": " + capitals[country])
#     else:
#         print('В базе нет страны с названием ' + country)
#---------------------------------------------------------
# goods = {
#     '1': ['Core-i3-4330', 9, 4500],
#     '2': ['Core i5-4670K', 3, 8500],
#     '3': ['AMD FX-6300', 6, 3700],
#     '4': ['Pentium G3220', 8, 2100],
#     '5': ['Core i5-3450', 5, 4600],
# }
#
# for i in goods:
#     print(i, ') ', goods[i][0], " - ", goods[i][1],  " шт. по ", goods[i][2], " руб", sep="")
#
# while True:
#     n = input("№: ")
#     if n != '0':
#         cnt = int(input("Количество: "))
#         goods[n][1] = cnt
#     else:
#         break
#
# for i in goods:
#     print(i, ') ', goods[i][0], " - ", goods[i][1],  " шт. по ", goods[i][2], " руб", sep="")
#--------------------------------------------------------
# d = {'a': 1, 'b': 2, 'c': 3}
# # print(d['b'])
# # a = 12
# # value = d.get('e', a)
# # print(value)
# # print(d)
# # # item = d.items()
# # # print(item)
# # # key = d.keys()
# # # print(key)
# # # value = d.values()
# # # print(value)
# # #
# # # for i, j in d.items():
# # #     print(i, "-> ", j)
# # #---------------------------------------------------------
# #
# # #---------------------------------------------------------
# #
# # #---------------------------------------------------------
# #
# # #---------------------------------------------------------
# # # d.clear()
# # # item = d.pop('b', 5)
# # # print(item)
# # # it = d.setdefault('e')
# # # print(it)
# # d.update([{'a', 7}, {'q', 9}]) #d.update([('r', 7), ('q', 9)])
# # print(d)
# d2 = d.copy()
# print("D =", d)
# print("D2 =", d2)
# d['e'] = 7
# d2['b'] = 5
# print("D =", d)
# print("D2 =", d2)
#--------------------------------------------------------
# a = {'a': 1, 'b': 2}
# b = {'b': 3, 'c': 4}
# c = a.copy()
# c.update()
# c = b | a
# print(c)
#--------------------------------------------------------
# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# new_d = dict()
# d['location'] = d.pop('city')
# new_d['name'] = d.pop('name')
# new_d['salary'] = d.pop('salary')

# print(d)
# print(new_d)
#--------------------------------------------------------
# a = {
#     'First': {
#         1: 'one',
#         2: 'two',
#         3: 'three'
#     },
#     'Second': {
#         4: 'four',
#         5: 'five'
#     }
# }
# print(a)
#
# for x in a:
#     print(x)
#     for y in a[x]:
#         print('\t', y, ": ", a[x][y], sep="")
#--------------------------------------------------------
# d = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}
# a = {value: key for key, value in d.items() if value <= 2}
# print(a)
#--------------------------------------------------------
# a = {i: i * 5 for i in [10, 20, 30, 40]}
# print(a)
#--------------------------------------------------------
# a = {i: i * 5 for i in "Hello"}
# print(a)
#--------------------------------------------------------
# value = int(input('-> '))
# it = [1, 2, 3, 4, 5]
# a = {i: value for i in range(1, 9)}
# print(a)
#
# d = dict.fromkeys(['a', 'b'], 100)
# print(d)
#--------------------------------------------------------
#list()
# figures = {1: 'Rectangle', 2: 'Triangle', 3: 'Circle'}
# value = list(figures.keys())
# value = list(figures.values())
# value = list(figures.items())
# print(value)
#--------------------------------------------------------
# a = ['one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four', -20]
# d = dict()
# s = None
#
# for i in a:
#     if type(i) == str:
#         d[i] = []
#         s = i
#     else:
#         d[s].append(i)
# print(d)
#--------------------------------------------------------
# zip

# d = (zip([12, 1, 2], ['Dec', 'Jan', 'Feb']))
# print(d)

# a = [12, 1, 2]
# b = ['Dec', 'Jan', "Feb"]
# f = {k: v for k, c in zip(b, a)}
# print(f)
#--------------------------------------------------------
# a = [1, 2, 3]
# print(list(zip(a)))
#
# print(list(zip(range(5), range(100))))
#--------------------------------------------------------
a = {'name': 'Igor', 'last_name': 'Doe', 'job': 'Concultant'}
b = {'name': 'Irina', 'last_name': 'Smith', 'job': 'Manager'}

for (k1, v1), (k2, v2), (k3, v3) in zip(a.items(), b.items(), c.items()):
    print(k1, '-> ', v1)
    print(k2, '-> ', v2)
    print(k3, '-> ', v3)
#--------------------------------------------------------

#--------------------------------------------------------

#--------------------------------------------------------

#--------------------------------------------------------











