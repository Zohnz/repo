import re

str1 = '1X, TEXT ABC 123 A1B2C3'
reg1 = r'\D(\d)'
print(re.findall(reg1, str1))


str2 = 'text from #START# till #END#'
reg2 = r'(?<=#START#).*?(?=#END#)'
# reg2 = r'(\d)[^\d\s]|[^\d\s](\d)'
#reg2 = r'\D(\d)'
print(re.findall(reg2, str2))


str3 = '12_34__56'
reg3 = r'(\d+)_[^_]'
print(re.findall(reg3, str3))
#
# def func(n):
#     if len == 0:
#         return 0
#     else:
#         res = func(n[1:])
#         if n[0] < 0:
#             res += 1
#             return res
#
#
# print('n =', func([-2, 3, 8, -11, -4, 6]))

# Файлы

# f = open('text.txt', mode='r')
# print(f)
# print(*f)
# f.close()
# print(f.closed)
# print(f.made)
# print(f.name)
# print(f.encoding)
#
# f = open('text.txt', 'r')
# print(f.read(3))
# print(f.read())
# f.close()


















