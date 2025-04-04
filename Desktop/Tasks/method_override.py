class Adult:
    def __init__(self, name, age, hair_color, eye_color):
        self.name = name
        self.age = age
        self.hair_color = hair_color
        self.eye_color = eye_color
    def can_drive(self):
        print(f"{self.name} is old enough to drive.")

class Child(Adult):
    def can_drive(self):
        print(f"{self.name} is too young to drive.")

name = input("Enter name: ")
age = int(input("Enter age: "))
hair_color = input("Enter hair color: ")
eye_color = input("Enter eye color: ")

person = Adult(name, age, hair_color, eye_color) if age >= 18 else Child(name, age, hair_color, eye_color)
person.can_drive()