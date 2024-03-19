# Class
class Person:

    #attributes
    def __init__(self, name, age, gender):  
        self.name = name 
        self.age = age 
        self.gender = gender 

    #method 
    def introduce(self):
        print(f'Greetings, I am called {self.name}, I am {self.age} years old and I identify as a {self.gender}.')
 
# instance 
person = Person(
    name = 'Kenick ohns',
    age = 22,
    gender = 'Male')

#output
person.introduce()