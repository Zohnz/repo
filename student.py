class Student:


    def init(self, name):
    self.name = name


def print_info(self):
    print("Student name:", self.name)


class Laptop:
    def __init__(self, model, processor, memory):
        self.model = model
        self.processor = processor
        self.memory = memory

    def print_info(self):
        print("Laptop model:", self.model)
        print("Laptop processor:", self.processor)
        print("Laptop memory:", self.memory)


student1 = Student("Roman")
student2 = Student("Vladimir")

laptop1 = student1.Laptop("HP", "i7", 16)
laptop2 = student2.Laptop("HP", "i7", 16)

student1.print_info()
laptop1.print_info()

student2.print_info()
laptop2.print_info()
