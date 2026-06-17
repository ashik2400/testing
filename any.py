# def squares(n):
#   for i in range(n):
#     yield i*i
  
# print(list(squares(5)))
import time

def timer(func):

    def wrapper():
        start = time.time()

        func()

        end = time.time()
        print("Execution Time:", end - start)

    return wrapper

@timer
def task():
    for i in range(1000000):
        pass

task()