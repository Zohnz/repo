# Задача 1

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
for i in range(a, b+1):
    if(i % 2 != 0):
        print(i)


#---------------------------------------------
# Задача 2

x = 35

i = 0
attempt = 0

while i != x:
    i = int(input("Введи число от 1 до 100:\n"))

    attempt = attempt + 1

    if i < x:
        print("Задуманное число больше")
    elif i > x:
        print("Задуманное число меньше")
    elif i == x:
        print("Вы угадали число за " + str(attempt) + "попыток")
    if i == 0:
        print("Выход")
        break

#------------------------------------------------------
# Задача 3

size = int(input("Введите размер поля: "))
symbol = int(input("Введите количество символов: "))
for i in range(size):
    for j in range(symbol):
        for n in range(size):
            for m in range(symbol):
                if (i + n) % 2 == 0:
                    print("*", end="")
                else:
                    print(" ", end="")
        print()