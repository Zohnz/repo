# 'Замените в этой строке все появления буквы 'о' на букву 'О', кроме первого и последнего вхождения."

s = input()
s = s.replace('о', '0', s.count('о') - 1)
s = s.replace('0', 'о', 1)
print(s)
