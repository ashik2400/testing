#

# print(even_square_list)

# square = [x**2 for x  in range(20) if x%2 == 0]
# print(square)

# square = {x**2 for x in range(11)}
# print(square)

# dict_comp = {word : len(word) for word in ["apple","banana","kiwi"]}
# print(dict_comp)

# def summarize(*args):
#   sum1 = sum(args)
#   average = sum1/len(args)
#   print(sum1)
#   print(average)

# summarize(10,20,30,40)

# def display_info(**kwargs):
#   for key,value in kwargs.items():
#     print(f'{key} : {value}')

# def even_numbers(n):
#     for i in range(n + 1):
#         if i % 2 == 0:
#             yield i

# for num in even_numbers(10):
#     print(num)

# import time

# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()      # Start time

#         result = func(*args, **kwargs)

#         end = time.time()        # End time
#         print(f"Execution time: {end - start:.4f} seconds")

#         return result
#     return wrapper


# @timer
# def slow_function():
#     time.sleep(2)  # Simulate a slow task
#     print("Function completed")


# slow_function()

# with open("notes.txt", "r") as file:
#     content = file.read()
#     print(content)

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def introduce(self):
        print(f"Hi, I'm {self.name} and my grade is {self.grade}")


class MScStudent(Student):
    def __init__(self, name, grade, specialization):
        super().__init__(name, grade)  # Initialize parent attributes
        self.specialization = specialization

    def introduce(self):  # Override parent method
        print(
            f"Hi, I'm {self.name}, my grade is {self.grade}, "
            f"and my specialization is {self.specialization}"
        )


# Create objects
student1 = Student("Ashik", "A")
msc_student1 = MScStudent("Ashik", "A", "Computer Science")

student1.introduce()
msc_student1.introduce()