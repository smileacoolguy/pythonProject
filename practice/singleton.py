class SingletonClass:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

obj1 = SingletonClass()
obj2 = SingletonClass()

print(obj1 is obj2)

