class A:

    @staticmethod
    def deco(func):
        def wrapper(*args, **kwargs):
            print("started")
            func(*args, **kwargs)
            print(str(func.__name__))
            print("ended")

        return wrapper

    @deco
    def impl(self):
        print("actual function run")

    def poly(self):
        print("From A")


a = A()
a.impl()
a.poly()

print("#"*100)
# encapsulation, inheritance, polymorphism, class

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
# print(o.__getattribute__())
## encapsulation
print(o.get_name())
o.set_name("Sana")
print(o.get_name())
#inheritance
o.impl()

#polymosphism
o.poly()