

class MyClass:
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            print("Decorator is doing something before the static method call.")
            if args[0] <= 0 or args[1] <= 0:
                print("ERROR One of the arguments is not positive: "+str(args))
                return False
            else:
                result = func(*args, **kwargs)
                print("Decorator is doing something after the static method call.")
                return result

        return wrapper

    @my_decorator  # Apply your custom decorator first
    @staticmethod
    def my_static_method(x, y):
        print(f"Executing static method with arguments: {x}, {y}")
        return x + y

try:
    # Call the decorated static method
    result = MyClass.my_static_method(5, 3)
    print(f"Result from static method: {result}")

    result = MyClass.my_static_method(-5, 3)
    if 'result' in locals():
        print(f"Result from static method: {result}")
finally:
    pass