sum = 0
x = int(input("Введите пятизначное число "))
y = len(x)


for i in sum:
    if (i % 2 != 0):
        sum *= i
        print(i)

print("Сумма всех нечетных чисел :  ",sum)