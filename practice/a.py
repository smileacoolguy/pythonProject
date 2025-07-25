class A:

    @staticmethod
    def deco(func):
        def wrapper(*args, **kwargs):
            print("function started")
            func(*args, **kwargs)
            print(str(func.__name__))
            print("function ended")

        return wrapper

    @deco
    def impl(self):
        print("actual function run")

    def poly(self):
        print("From class A")


a = A()
a.impl()
a.poly()

print("#"*100)


class Oops(A):
    """this is intro"""
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def poly(self):
        print("From " + Oops.__name__)

o=Oops("Ismail","01")

print(Oops.__dict__)
print("#"*100)

print(o.get_name())
o.set_name("QA")
print(o.get_name())

o.impl()

o.poly()

x = [1, 2, 3]
y = [1, 2, 3]
print(x == y, x is y)

x = lambda a, b: a + b
print(x(2, 3))

