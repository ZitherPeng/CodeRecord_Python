class Sdudent(object):


    # construction method
    def __init__(self, name, score):
        self.name = name
        self.score = score

    # 类方法
    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

zither = Sdudent('peng',12)
print(zither)
print(Sdudent)

print(zither.name)
zither.name = 'zitherpeng'

print(zither.name)
print(zither.score)

zither.print_score()

print(zither.get_grade())