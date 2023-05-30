# def CalcSumNegativeNumbers(A):
#     if A == []:
#         return 0
#     else:
#         count = CalcSumNegativeNumbers(A[1:])
#         if A[0] < 0:
#             count = count + 1
#
#         return count
#
#
# b = [-2, 3, 8, -11, -4, 6]
# n = CalcSumNegativeNumbers(b)
# print("n = ", n)

# ---------------------Task 2---------------------------------
listt = ['Adam', ['Bob', ['Chet', 'Cat'], 'Bard', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']

def a(element):
    count = 0
    if isinstance(element, list):
        for each_element in element:
            count += a(each_element)
    else:
        count += 1
    return count

print(a(listt))