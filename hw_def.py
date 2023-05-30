# ---------------------------Task 1-------------------------------------
# def prod(*nums):
#
#     prd = 1
#     for n in nums:
#         prd *= n
#
#     print("Произведение: ", prd)
#
# prod(10, 9)
# prod(2, 3, 4)
# prod(3, 5, 10, 6)

# ---------------------------Task 2-------------------------------------

# def func(*args):
#
#     s = 0
#     for i in args:
#         s += i
#         print(s, end=' ')
#     print()
#
#
# func(3, 9, 1)
# func(2, 5, 4, 2)
# func(3, 5, 10, 6, 3)

# ---------------------------Task 3-------------------------------------

def func(figure_type, **kwargs):
    if figure_type == 'rhombus':
        s = (kwargs['d1'] * kwargs['d2']) / 2
        return s
    if figure_type == 'square':
        s = (kwargs['a'])**2
        return s
    if figure_type == 'trapezoid':
        s = ((kwargs['a'] + kwargs['b']) / 2) * (kwargs['h'])
        return s
    if figure_type == 'circle':
        import math
        s = math.pi * (kwargs['r'] ** 2)
        return s


print(func(figure_type='rhombus', d1 = 10, d2 = 8))
print(func(figure_type='square', a = 5))
print(func(figure_type='trapezoid', a = 12, b = 3, h = 6))
print(func(figure_type='circle', r = 18))
print(func(figure_type='unknown', a = 1, b = 2, c = 3))
