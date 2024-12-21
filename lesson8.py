class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

my_rectangle = Rectangle(5,3)

area = my_rectangle.calculate_area()
perimeter = my_rectangle.calculate_perimeter()

print(f"Area: {area}")
print(f"perimeter: {perimeter}")
class Person:
    def __init__(selfself, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"hello, i am {self.name}, and i am {self.age} years old")

person1 = person("arion",21)
person2 = person("camavinga",23)

person1.greet()
person2.greet()