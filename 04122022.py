# with open('text4.txt', 'w+') as f:
#     print(f.write('0123456789'))

# with open('text2.txt', 'r') as f:
#     for line in f:
#         print(line[:6])
#
# file_name = 'res.txt'
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
#
#
# def get_line(lt):
#     lt = list(map(str, lt))
#     return ' '.join(lt)
#
#
# with open(file_name, 'w') as f:
#     f.write(get_line(lst))
# print(get_line(lst))


with open(file_name, 'r') as f:
    nums = f.read()

print(nums)

lst = map(float, nums.split(' '))
print(lst)
print(len(lst))
print(sum(lst))

















































