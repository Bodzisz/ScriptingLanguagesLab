import time

def timer(func):
    def wraper():
        before = time.perf_counter()
        func()
        after = time.perf_counter()
        print(str(round(after - before, 2)))
    return wraper

@timer
def factorial():
    result = 1
    for i in range(100000000):
        result = result * i
    return result

factorial()