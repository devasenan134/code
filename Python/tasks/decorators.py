'''
def decorator_X(func):
    def wrapper_func():
        print("X" * 10)
        func()
        print("X" * 10)

    return wrapper_func

def decorator_Y(func):
    def wrapper_func():
        print("Y" * 10)
        func()
        print("Y" * 10)

    return wrapper_func


@decorator_X
@decorator_Y     # alternate for the below two lines
def say_hello():
    print("Hello world")

say_hello()
# hello = decorator_X(say_hello)   # creating decorator
# hello = decorator_Y(decorator_X(say_hello))
# hello()
'''



# With parameters
def decorator_divide(func):
    def wrapper_func(a, b):
        print("divide ", a, "and ", b)
        if b == 0:
            print("division with zero is not allowed")
            return
        result = func(a, b)
        print("end of decorator")
        return result       

    return wrapper_func
 

@decorator_divide
def divide(x, y):
    print("inside func")                
    return x / y                    # so what clear with return in decorators
    


print(divide(10, 2))