from time import time


def timings(func):
    def wrapper_func(*args, **kwargs):
        start = time()
        print("Start")
        result = func(*args, **kwargs)
        end = time()
        print("End")
        print(f"Elapsed time: {end - start}")
        return result
    
    return wrapper_func


@timings
def my_func(num):
    sum = 0
    for i in range(num+1):
        sum += i
    return sum


print(my_func(3000000))