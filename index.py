class Student:
    def __init__(self, name, age):
        self.__name = name    
        self.__age = age


    def get_name(self):
        return self.__name


    def set_name(self, name):
        if name:
            self.__name = name


    def get_age(self):
        return self.__age


    def set_age(self, age):
        if 5 <= age <= 100:
            self.__age = age
        else:
            print("Invalid age")


student1 = Student("John", 20)
print("Name:", student1.get_name())
print("Age:", student1.get_age())

student1.set_name("Jane")
student1.set_age(22)

print("Updated Name:", student1.get_name())
print("Updated Age:", student1.get_age())
