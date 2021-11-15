class A:
    def __init__(self):
        self.cal = 7

class B:
    def cal(self):
        return 3

class C(A, B):
    pass


c = C()
print (c.cal)
