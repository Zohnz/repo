def func(s):
    a = ''
    while s > 0:
        a = str(s % 2) + a
        s //= 2
    return a


while 1:
    s = int(input("Введите десятичное число: "))
    if s != 0:
        print(func(s))
    else:
        break
