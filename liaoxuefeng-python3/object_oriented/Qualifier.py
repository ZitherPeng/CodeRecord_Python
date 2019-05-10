import time


class Sdudent(object):

    # construction method
    def __init__(self, name, score, gender):
        self.name = name
        self.score = score
        self.__gender = gender

    # construction method
    def __init__(self, name, birth=time.time()):
        self.name = name
        self.__birth = birth  # private

    # 类方法
    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def print_birth(self):
        print('%s: %s' % (self.name, self.__birth))

    def print_gender(self):
        print('%s: %s' % (self.name, self.__gender))


zither = Sdudent('zither')
zither.print_birth()

foo = Sdudent('Luckycoding', 12, 'male')

print(foo.__gender)

print(foo._Sdudent__gender)
pass
