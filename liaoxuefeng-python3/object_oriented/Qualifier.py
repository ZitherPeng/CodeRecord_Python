import time

class Sdudent(object):

    # construction method
    def __init__(self, name, score):
        self.name = name
        self.score = score

    # construction method
    def __init__(self, name, birth=time.time()):
        self.name = name
        self.__birth = birth  # private


    # 类方法
    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def print_birth(self): 
        print('%s: %s' % (self.name, self.__birth))


zither = Sdudent('zither')
zither.print_birth()
