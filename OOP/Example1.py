

class Human:

    def __init__(self, name , age, height):
        self.name = name
        self.age = age
        self.height = height

    def birthday(self):
         self.age += 1

oren = Human("oren",18,179)
print(oren.age)
oren.birthday()
print(oren.age)