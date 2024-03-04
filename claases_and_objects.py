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
    def add_skills(self, skills):
        self.skills.extend(skills)


ciroma = Person('Ciroma', 'Adekunle', 20, 'Nigeria', 'Ilorin')
ciroma.add_skills("Web Scraping", "HTMl", "CSS", "Python", "Corel")

john = Person()
print(john.info())
print(ciroma.info())
print(ciroma.firstname)
print(ciroma.lastname)
print(ciroma.age)
print(ciroma.country)
print(ciroma.city)
print(ciroma.skills)