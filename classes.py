class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print("move")

    def draw(self):
        print("draw")

# an object is an instance of a class
point1 = Point(10, 12)
# print(point1.x)
point1.draw()

class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi i am {self.name}")


person = Person("Jon Snow")
person.talk()

# Inheritance
class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    pass


class Cat(Mammal):
    def be_chilling(self):
        print("chilling")


dog = Dog()
dog.walk()

# modules
