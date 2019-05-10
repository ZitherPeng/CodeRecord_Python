def calc():
    pass


def add_end(L=[]):
    L.append('END')
    return L


print(add_end())
print(add_end())


# 默认参数必须之向不变的对象，否则可能发生改变
def add_end_fix(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


print(add_end_fix())
print(add_end_fix())


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


num = [4, 3, 2, 1]
print(calc(1, 2))
print(calc(*num))


def person(name, age, **kwargs):
    print(name,age, kwargs)

person('zither',12,city='shanghai')

attr={'gender':'male','store':'A'}

person('zither',12,**attr)

def animal(*args, **kwargs):
    print(args,kwargs)

animal('peiqi', 'pig', 12, home="shanghai", time='now')

args = (1,2,3)
kw = {'a':'1'}

person(*args,**kw)

