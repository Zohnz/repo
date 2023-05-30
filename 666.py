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


