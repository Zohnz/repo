class Car:
    def __init__(self, model, year, manufacturer, engine_power, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_power = engine_power
        self.color = color
        self.price = price

    def set_model(self, model):
        self.model = model

    def set_year(self, year):
        self.year = year

    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def set_engine_power(self, engine_power):
        self.engine_power = engine_power

    def set_color(self, color):
        self.color = color

    def set_price(self, price):
        self.price = price

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_manufacturer(self):
        return self.manufacturer

    def get_engine_power(self):
        return self.engine_power

    def get_color(self):
        return self.color

    def get_price(self):
        return self.price

    def input_data(self):
        self.set_model(input("Введите название модели: "))
        self.set_year(input("Введите год выпуска: "))
        self.set_manufacturer(input("Введите производителя: "))
        self.set_engine_power(input("Введите мощность двигателя: "))
        self.set_color(input("Введите цвет: "))
        self.set_price(input("Введите цену: "))

    def output_data(self):
        print("Название модели:", self.get_model())
        print("Год выпуска:", self.get_year())
        print("Производитель:", self.get_manufacturer())
        print("Мощность двигателя:", self.get_engine_power())
        print("Цвет:", self.get_color())
        print("Цена:", self.get_price())


car1 = Car("X7 M05i", "2021", "BMW", "530 л.с.", "white", "10790000")
car1.output_data()