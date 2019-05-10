import types

'''
对象信息
'''


class Animal:
    pass


a = Animal()
print(type(a))

foo = type(123) == type(345)


def func_check(function):
    if type(function) == types.FunctionType:
        print(function.__str__() + ' is a function')
        print(function.__code__.co_name + 'is a function')


func_check(func_check)


class Dog(Animal):
    pass


print(isinstance(Dog(), Animal))
print(isinstance(Dog(), Dog))
print(isinstance(Dog(), (Dog, Animal)))

print('*' * 10)
'''
对象属性操作
'''


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


print(hasattr(MyObject(), 'x'))
foo = MyObject()
setattr(foo, 'y', 12)
print(hasattr(foo,'x'))


