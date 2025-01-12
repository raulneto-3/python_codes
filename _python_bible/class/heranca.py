class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_older(self, years):
        self.age += years

class Programmer(Person):
    def __init__(self, name, age, language):
        super().__init__(name, age)
        self.language = language

    def print_language(self):
        print("Language: {}".format(self.language))

##########################################################
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Some sound!")

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
    
    def make_sound(self):
        print("Bark!")
