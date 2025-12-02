from functools import wraps
def my_decorator(func: function):
    @wraps(func) #This maintains the function metadata, if this line is commented the 15th line shows wrapper as value
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper

@my_decorator
def greet():
    print("Hello From Decorators class from Chai Code")

greet()
print(greet.__name__) #This returns the wrapper function instead of greet function if 3rd line is not present