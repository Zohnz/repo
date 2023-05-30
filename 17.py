# string = 'Ежевику для ежат принесли два ежа. Ежевику еле-еле ежата возле ели съели'
#
# result = len(list(filter(lambda s: s.lower().startswith('е'), string.split())))
# print(result)

#-------------------------------------

# text = 'Дана ст(рока символов, среди которых есть одна открыв)ающаяся'
# i = 0
# while text[i] != '(':
#     i += 1
# i += 1
# while text[i] != ')':
#     print(text[i], end='')
#     i += 1

#---------------------------------------
s, s1, s2 = input(), input(), input()
print(s.replace(s1, s2))