class Animal(object):
    def run(self):
        print('Animal is run')

class Dog(Animal):
    def run(self):
        # 多态：重写
        print('Dog is run')

class Cat(Animal):
    pass

dog = Dog()
dog.run()

def run_twice(animal):
    animal.run()

run_twice(Dog())

