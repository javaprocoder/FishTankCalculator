# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

# class Student(Person):
#     pass


#--------------Print A--------------
# class Base:
#     def __init__(self):
#         self._a = "a"
#         self._c = "ccc"

#     def access_c(self):
#         return self._c

#     def access_a(self):
#         return self._a

# x = Base()
# print(x.access_a())

#--------------Classes and Usage--------------
class Animal:
    def speak(self):
        print("Some Sound!")

class Dog(Animal):
    def speak(self):
        print("Bow Bow!")

class Cat(Animal):
    def speak(self):
        print("Meow Meow!")

a = Animal()
a.speak

b = Dog()
b.speak

#--------------Polymorphism Principle--------------
def add(num1, num2, num3=0):
    return num1+num2+num3

print(add(1,2))
print(add(1,2,3))
