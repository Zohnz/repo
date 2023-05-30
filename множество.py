# a = {0, 1, 2, 3}
# a.add(4)
# print(a)
#---------------------------------------------------------
# a = {'Tom', 'Bob', 'Alice'}
# a.add('Ann')
# print(a)
# # a.remove('Tom')
# # print(a)
# # user = 'Tom'
# # if user in a:
# #     a.remove(user)
# #     print(a)
# #
# # a.discard('Bob')
# # print(a)
# a.pop()
# print(a)
#---------------------------------------------------------

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# # c = a.union(b)
# # c = a | b
# # print(c)
# # a.update(b)
# # a |= b
# # print(a)
# # c = a & b
# # print(c)
# # a &= b
# # print(a)
# # c = a - b
# # print(c)
# c = a ^ b
# print(c)
#---------------------------------------------------------
# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
#
# # s = s1.union(s2, s3, s4, s5, s6, s7)
# s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# print(s)
#
# print(len(s))
# print(min(s))
# print(max(s))
# print(sum(s))
#---------------------------------------------------------

# s1 = "Hello"
# s2 = "How are you"
# s = set(s1) & set(s2)
# print(s)
#---------------------------------------------------------

# s1 = "Python"
# s2 = "Programming language"
# s = set(s1) - set(s2)
# print(s)
#---------------------------------------------------------
# s1 = set('Python')
# s2 = set('Programming language')
# s = s1 - s2
# print(s)
#---------------------------------------------------------

# drawing = {'Marina', 'Jenya', 'Sveta'}
# music = {'Kostya', 'Jenya', 'Ilya'}
# only = drawing ^ music
# print('Одно хобби: ', only)
#
# both = drawing & music
# print('Два хобби ', both)
#
# drawing = drawing - both
# print(drawing)
#---------------------------------------------------------
# b = [1, 2, 3, 4, 5]
# s = frozenset(b)
# print(s)
# c = [0, 1, 2]
# s1 = frozenset(c)
# print(s1)
# s -= s1
# print(s)
# s = frozenset([1, 2, 3, 4, 5])
# print(s)


# a = frozenset({"hello", "world"})
# print(a)


