class A:
    def __init__(self):
        pass

    def b(self):
        aa = A()
        bb = A()
        print id(aa), id(bb)

a = A()
a.b()
