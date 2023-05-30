import random


class Cat:
    def __init__(self, age, name, pol):
        self.name = name
        self.pol = pol
        self.age = age

    def __str__(self):
        if self.pol == "M":
            return f"{self.name} is good boy!!!"
        elif self.pol == "F":
            return f"{self.name} is good girl!!!"
        else:
            return f"{self.name} is good Kitty!!!"

    def __repr__(self):
        return f"Cat(name='{self.name}', age= {self.age}, sex='{self.pol}')"

    def __add__(self, other):
        a = [Cat("Ron", 3, "M")]
        print("!!!!!!!!!!!!!!!!!", a)
        if self.pol != other.pol:
            return [Cat("No name", 0, random.choice(['M', 'F'])) for _ in range(3, random.randint(2, 7))]
        else:
            #return "Types are not support!"
            raise TypeError("Types are not support!")


сat1 = Cat("Tom", 4, "M")
print(cat1)
cat2 = Cat("Elsa", 5, "F")
print(cat2)
print(cat1 + cat2)
cat3 = Cat("Ron", "M")
print(cat3)
print(cat1 + cat3)
lst = (cat1, cat2, cat3)
b, c = random.choices(lst, k=2)
print(b+c)