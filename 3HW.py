sum = 0
a = int(input("Введите начальное число:  "))
b = int(input("Введите конечное число:  "))

for i in range(a, b+1):
    if (i % 2 != 0):
        sum += i
        print(i)

print("Сумма всех нечетных чисел :  ",sum)




