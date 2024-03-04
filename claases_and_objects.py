class Person:
    def __init__(self, name):
        # self allows to attach parameter to the class
        self.name = name


p = Person('Ayobami')
print(p.name)
print(p)