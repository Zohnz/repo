from jinja2 import Template

# name = "Игорь"
# age = 28
# per = {'name': 'Игорь', 'age': 28}
# cities = [
#     {'id': 1, 'city': 'Москва'},
#     {'id': 1, 'city': 'Пенза'},
#     {'id': 1, 'city': 'Уфа'},
#     {'id': 1, 'city': 'Минск'},
#     {'id': 1, 'city': 'Киров'},
# ]
#
# link = """<select name="cities">
# {% for c in cities -%}
# {% if c.id > 3 -%}
#     <option value="{{c['id'] }}">{{ c.city }}</option>
#     {% elif c.city %}
# {% else -%}
#     {{ c['city'] }}
# {% endif -%}
# {% endfor -%}
# </select>"""
#
# tm = Template(link)
# msg = tm.render(cities=cities)
#
# print(msg)



menu = [    {'id': 'index', 'title': 'Главная'},
            {'id': 'news', 'title': 'Новости'},
            {'id': 'about', 'title': 'О компании'},
            {'id': 'shop', 'title': 'Магазин'},
            {'id': 'contacts', 'title': 'Контакты'},
            ]
link = """<ul>{%for i in menu -%}
{%if i.title=='Главная'-%}
<li><a href="/{{i.id}}" class="active">{{i.title}}</li>
{%else-%}<li><a href="/{{i.id}}">{{i.title}}
</li>{%endif-%}{%endfor-%}</ul>
"""
tm = Template(link)
msg = tm.render(menu=menu)
print(msg)



cars = [    {'model': 'Audi', 'price': 23000},
            {'model': 'Skoda', 'price': 17300},
            {'model': 'Renault', 'price': 44300},
            {'model': 'Wolksvagen', 'price': 21300}]

lst = [1, 2, 3, 4, 5, 6]
print(sum(cars['price']))
tp1 = "Суммарная цена автомобилей {{ cs }}"
tm = Template(tp1)
msg = tm.render(cs=cars)
print(msg)