# Задача 3

num = int(input("Введите номер операции: "))
res = "Ответ: "

if num == 1:
    a = int(input("Введите число: "))
    a = -a
    print(res, a)
else:
    b = int(input("Введите первое число: "))
    c = int(input("Введите второе число: "))
    if num == 2:
        print(res, b * c)
    elif num == 3:
        b = int(input("Введите первое число: "))
        c = int(input("Введите второе число: "))
        print(res, b - c)
    elif num == 4:
        b = int(input("Введите первое число: "))
        c = int(input("Введите второе число: "))
        if c == 0:
            print(res + "На ноль делить нельзя")
        else:
            print(res, b / c)
    elif num == 5:
        b = int(input("Введите первое число: "))
        c = int(input("Введите второе число: "))
        print(res, b * c)
    elif num == 6:
        b = int(input("Введите первое число: "))
        c = int(input("Введите второе число: "))
        print(res, b % c)
    elif num == 7:
        b = int(input("Введите первое число: "))
        c = int(input("Введите второе число: "))
        if b < c:
            print(res, str(b) + "меньше" + str(c))
        else:
            print(res, str(c) + "меньше" + str(b))
    elif num == 8:
        b = int(input("Введите первое число: "))
        c = int(input("Введите второе число: "))
        if b > c:
            print(res, str(b) + "больше" + str(c))
        else:
            print(res, str(c) + "больше" + str(b))

#Задача 2
a = int(input("Введите целое число:   "))

if (a % 2 == 1):
    print(f"Число {a} - нечетное")
else:
    print(f"Число {a} - четное")

# Задача 1

a = int(input("Введите пятизначное число: "))

sum = 0
prd = 1

while (a != 0):
    prd = prd * (a % 10)
    a = a // 10
while (a > 0):
    remainder = a % 10
    sum = sum + remainder
    a = a // 10
print("Среднее арифметическое равно: ", sum // 5)
print("Произведение цифр равно: ", prd)