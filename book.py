class Book:
    def __init__(self, title=None, year=None, publisher=None, genre=None, author=None, price=None):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def set_title(self, title):
        self.title = title

    def set_year(self, year):
        self.year = year

    def set_publisher(self, publisher):
        self.publisher = publisher

    def set_genre(self, genre):
        self.genre = genre

    def set_author(self, author):
        self.author = author

    def set_price(self, price):
        self.price = price

    def get_title(self):
        return self.title

    def get_year(self):
        return self.year

    def get_publisher(self):
        return self.publisher

    def get_genre(self):
        return self.genre

    def get_author(self):
        return self.author

    def get_price(self):
        return self.price

    def input_book(self):
        self.set_title(input('Введите название книги: '))
        self.set_year(input('Введите год выпуска книги: '))
        self.set_publisher(input('Введите издателя книги: '))
        self.set_genre(input('Введите жанр книги: '))
        self.set_author(input('Введите автора книги: '))
        self.set_price(input('Введите цену книги: '))

    def print_book(self):
        print('Название книги:', self.get_title())
        print('Год выпуска:', self.get_year())
        print('Издательство:', self.get_publisher())
        print('Жанр:', self.get_genre())
        print('Автор:', self.get_author())
        print('Цена:', self.get_price())