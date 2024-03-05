"""
class Person:
    def __init__(self, name):
        # self allows to attach parameter to the class
        self.name = name


p = Person('Ayobami')
print(p.name)
print(p)

"""
class Person:
    def __init__(self, firstname="John", lastname="Doe", age=20, country="Morocco", city="Rabat"):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
        self.skills = []
    def info(self):
        return f"{self.firstname} {self.lastname} is {self.age} years old and lives in {self.city}, {self.country}"
    def add_skills(self, *skills):
        self.skills.append(skills)
# Creating a class called Student that is Inheriting from Person
class Student(Person):
    # Defining a constructor function in the Child Class
    def __init__ (self, firstname='Ciroma', lastname='Adekunle',age=25, country='Finland', city='Helsinki', gender='male'):
        self.gender = gender
        super().__init__(firstname, lastname,age, country, city)

    def info(self):
        gender = 'He' if self.gender == 'male' else 'She'
        return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'

# Instatiating an object from class Person
# ciroma = Person('Ciroma', 'Adekunle', 20, 'Nigeria', 'Ilorin')
# Writing a method  that modifies Class default values
# ciroma.add_skills("Web Scraping", "HTMl", "CSS", "Python", "Corel")
student1 = Student("Jordan", "Walke", 20, "Indonesia", "Jakarta")
print(student1.firstname)
student1.add_skills("Typing", "Dancing")
print(student1.skills)
print(student1.info())
# john = Person()
# print(john.info())
# print(ciroma.info())
# print(ciroma.firstname)
# print(ciroma.lastname)
# print(ciroma.age)
# print(ciroma.country)
# print(ciroma.city)
# print(ciroma.skills)