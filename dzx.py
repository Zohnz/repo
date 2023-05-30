
#for num in range (a, b + 1):
   # if num % 2! == 0:
    #    print(num, b = " ")


def sumoddnum(s):
    total= 0
    for i in range(len(s)):
        if i % 2 == 1:
            total += i
    return total
print(sumoddnum('12345'))