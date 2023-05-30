# import random
#
#
# class Cat:
#     def __init__(self, age, name, pol):
#         self.name = name
#         self.pol = pol
#         self.age = age
#
#     def __str__(self):
#         if self.pol == "M":
#             return f"{self.name} is good boy!!!"
#         elif self.pol == "F":
#             return f"{self.name} is good girl!!!"
#         else:
#             return f"{self.name} is good Kitty!!!"
#
#     def __repr__(self):
#         return f"Cat(name='{self.name}', age= {self.age}, sex='{self.pol}')"
#
#     def __add__(self, other):
#         a = [Cat("Ron", 3, "M")]
#         print("!!!!!!!!!!!!!!!!!", a)
#         if self.pol != other.pol:
#             return [Cat("No name", 0, random.choice(['M', 'F'])) for _ in range(3, random.randint(2, 7))]
#         else:
#             #return "Types are not support!"
#             raise TypeError("Types are not support!")
#
#
# сat1 = Cat("Tom", 4, "M")
# print(cat1)
# cat2 = Cat("Elsa", 5, "F")
# print(cat2)
# print(cat1 + cat2)
# cat3 = Cat("Ron", "M")
# print(cat3)
# print(cat1 + cat3)
# lst = (cat1, cat2, cat3)
# b, c = random.choices(lst, k=2)
# print(b+c)


#-------------------------------------------------

from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def get_per(self):
        pass

    def get_area(self):
        raise NotImplementedError("В дочернем классе должен быть определен метод get_area")
#------------------------------------------------------
#     class Shape():
#         def __init__(self, color):
#             self.color = color
#
#
# class Triangle:








     def draw(self):
         lst = [self.a, self.b, self.c]
         rows = []
         n = min(lst)
         for i in range(n):
             rows = ['-' * (n - i - 1) + '*' * (2 * i + 1) for i in range(n)]
            return '\n'.join(rows)



class Shape:
    def __init__(self, color):
        self.color = colorclass Triangle(Shape):
        def __init__(self, a, b, c, color):
            super().__init__(color)
            self.a = a
            self.b = b
            self.c = c
            # def draw(self): # 11, 6, 6
            #     lst = [self.a, self.b, self.c]
            #     n = min(lst) # 6
            #     for i in range(n): # 1
            #  print('-' * (n - i - 1) + '*' * (2 * i + 1))  # "-" * 4 + "*" * 3

            def draw(self):
                lst = [self.a, self.b, self.c]
                n = min(lst)
                rows = [' ' * (n - i - 1) + '*' * (2 * i + 1) for i in range(n)]
                return '\n'.join(rows)


            t = Triangle(11, 6, 6, "yellow")
            # t.draw()
            print(t.draw())



   #--------------------------------------
#class MyDecorator:
#    def __init__(self, fn):
 #       self.func = fn

 #   def __call__(self):
  #      print('перед вызовом функции')
#        self.func()
#        print('после вызова функции')

        class MyDecorator(fn):
            def wrap():
                print('перед вызовом функции')
                fn()
                print('после вызова функции')

            return wrap


@MyDecorator
def func():
    print("func")


func()