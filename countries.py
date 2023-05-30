countries = {
    "Россия": "Москва",
    "США": "Вашингтон",
    "Китай": "Пекин"
}

def add_country(countries):
    country = input("Введите название страны (с заглавной буквы): ")
    capital = input("Введите название столицы страны (с заглавной буквы): ")
    countries[country] = capital
    print("Файл сохранен.")

def delete_country(countries):
    country = input("Введите название страны (с заглавной буквы): ")
    if country in countries:
        del countries[country]
        print("Файл сохранен.")
    else:
        print("Страна не найдена.")

def find_country(countries):
    country = input("Введите название страны (с заглавной буквы): ")
    if country in countries:
        capital = countries[country]
        print(f"Страна: {country}, Столица: {capital}")
    else:
        print("Страна не найдена.")

def edit_country(countries):
    country = input("Введите название страны (с заглавной буквы): ")
    if country in countries:
        new_capital = input("Введите новое название столицы страны (с заглавной буквы): ")
        countries[country] = new_capital
        print("Файл сохранен.")
    else:
        print("Страна не найдена.")

def view_countries(countries):
    for country, capital in countries.items():
        print(f"{country}: {capital}")

while True:
    print("Выберите действие:")
    print("1 - добавление данных")
    print("2 - удаление данных")
    print("3 - поиск данных")
    print("4 - редактирование данных")
    print("5 - просмотр данных")
    print("6 - завершение работы")

    choice = input("Ввод: ")
    if choice == "1":
        add_country(countries)
    elif choice == "2":
        delete_country(countries)
    elif choice == "3":
        find_country(countries)
    elif choice == "4":
        edit_country(countries)
    elif choice == "5":
        view_countries(countries)
    elif choice == "6":
        break
    else:
        print("Неверный выбор.")