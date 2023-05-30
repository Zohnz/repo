from jinja2 import Environment, FileSystemLoader

persons = [
    {"name": "Алексей", "year": 18, "weight": 78.5},
    {"name": "Никита", "year": 28, "weight": 82.3},
    {"name": "Виталий", "year": 33, "weight": 94.0}
]
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('main.html')
msg = tm.render(users=persons, title='About Jinja')

print(msg)
