# 1
# def hello_decorator(func):
#     def main():
#         print("Hello, World!")  
#         func()
#     return main

# @hello_decorator
# def my_function():
#     print("Salom jahon.")

# my_function()



# 2.
# def salom_decorator(message):
#     def decorator(func):
#         def main():
#             print(message) 
#             func()  
#         return main
#     return decorator

# @salom_decorator("Salom, Sunat!") 
# def my_function():
#     print("Ин функсияи ман аст.")


# my_function()



# 3.

# def main(my_function):
#     def hello():
#         nonlocal count
#         count += 1 
#         print(f"Функсия {count} маротиба даъват шудааст.")  
#         my_function()
#     count = 0
#     return hello

# @main
# def my_function():
#     print("Ин функсияи ман аст.")


# my_function()
# my_function()



# 4


# def decorator(func):
#     def salom():
#         print("Пеш аз даъват кардани функсия") 
#         func() 
#         print("Пас аз даъват кардани функсия")  
#     return salom

# @decorator
# def my_function():
#     print("Ин функсияи ман аст!")  


# my_function()


