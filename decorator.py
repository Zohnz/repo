def hi_decorator(func):
    def wrapper():
        print("Hi everyone!")
        func()

    return wrapper


@hi_decorator
def my_function():
    print("Welcome :)")


my_function()