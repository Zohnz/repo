# import re
#
# text = """
# Самара
# Москва
# Тверь
# Уфа
# Казань
# """
# count = 0
#
#
# def replace_find(m):
#     global count
#     count += 1
#     return f"<option value = '{count}'>{m.group(1)}</option>\n"
#
#
# print(re.sub(r"\s*(\w+)\s*", replace_find, text))
# ------------------------------------------------------
import re
#
# s = "<p>Изображение <img src='bg.jpg'> - фон страницы"
# reg = r'<img\s+[^>]*src=(?P<q>[\'"])(.+)(?P=q001)>'
# print(re.findall(reg, s))


# s = "Самолет прилетает 10/23/2023. Будем рады вас видеть после 10/24/2023."
# reg = r'(\d{2})/(\d{2})/(\d{4})'
# print(re.findall(reg, s))
# print(re.sub(reg, r'\2.\1.\3', s))


s = "google.com and google.ru"
reg = r'(([a-z0-9-]{2,}\.)+[a-z]{2,4})'
print(re.findall(reg, s))
print(re.sub(reg, r"http://\1", s))






















































