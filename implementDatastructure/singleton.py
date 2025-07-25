class SingletonClass:
    _instance = None  # Class variable to hold the single instance

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            # If no instance exists, create a new one
            cls._instance = super().__new__(cls)
        return cls._instance  # Return the existing instance

obj1 = SingletonClass()
obj2 = SingletonClass()

print(obj1 is obj2)  # Output: True