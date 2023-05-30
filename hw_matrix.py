# lst = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
#
# row = 0
# for row in lst:
#     for col in row:
#         print(col, end='\t')
#     print()
# print("-----------------------")
# i = 0
# for col in row:
#     for row in lst:
#         print(row[i], end='\t')
#     i += 1
#     print()

#--------------------------------------------------------------------------








# n, m = int(input('Введите высоту матрицы: ')), int(input('Введите ширину матрицы: '))
# matr = [[0 for i in range(m)] for j in range(n)]
# for row in matr:
#     for x in row:
#         print(x, end='\t')
#     print()