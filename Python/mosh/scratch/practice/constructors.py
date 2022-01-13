# python 3.7.1


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'Hi, I am {self.name}')
    
    
deva = Person("Devasenan")
# print(deva.name)
deva.talk()
