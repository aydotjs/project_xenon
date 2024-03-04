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
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
    def info(self):
        return f"{self.firstname} {self.lastname} is {self.age} years old and lives in {self.city}, {self.country}"

ciroma = Person('Ciroma', 'Adekunle', 20, 'Nigeria', 'Ilorin')
print(ciroma.info())
print(ciroma.firstname)
print(ciroma.lastname)
print(ciroma.age)
print(ciroma.country)
print(ciroma.city)