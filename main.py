from enum import Enum



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







#1. Напишите декоратор, который печатает «Функция вызвана» каждый раз при выполнении функции.
# def say_hello(func):
#     def main():
#         print("Функция вызвана")
#         func()
#     return main

# @say_hello
# def my_function():
#     print("Работа функции")

# my_function()



#2. Напишите декоратор, который выполняет некоторые действия до и после вызова функции (например, операторы печати).
# def say_hello(func):
#     def main():
#         print("До вызова функции")
#         func()
#         print("После вызова функции")
#     return main

# @say_hello
# def my_function():
#     print("Работа функции")

# my_function()



# 3. Определите Enum, представляющий дни недели, и напишите функцию для проверки того, является ли данный день будним или выходным.

# from enum import Enum

# class WeekDay(Enum):
#     MONDAY = 1
#     TUESDAY = 2
#     WEDNESDAY = 3
#     THURSDAY = 4
#     FRIDAY = 5
#     SATURDAY = 6
#     SUNDAY = 7

# def is_weekend(day):
#     if day in (WeekDay.SATURDAY, WeekDay.SUNDAY):
#         return "Выходной"
#     else:
#         return "Будний день"

# day = WeekDay.SATURDAY
# print(f"{day.name}: {is_weekend(day)}")

# day = WeekDay.WEDNESDAY
# print(f"{day.name}: {is_weekend(day)}")



# 4. Определите Enum для кодов состояния HTTP с числовыми значениями.

# from enum import Enum

# class Http(Enum):
#     SUCCESS = 200
#     CREATED = 201 
#     BAD_REQUEST  = 400
#     NOT_FOUND = 401
#     UNAUTHORIZED = 403 
#     FORBIDDEN  =404
#     INTERVAL_SERVER = 500


# print(Http.SUCCESS)
# print(Http.NOT_FOUND.value)









# # 5. Напишите функцию, которая принимает член перечисления в качестве аргумента и возвращает различные результаты в зависимости от значения перечисления.
# # from enum import Enum

# class Http(Enum):
#     SUCCESS = 200
#     CREATED = 201 
#     BAD_REQUEST  = 400
#     NOT_FOUND = 401
#     UNAUTHORIZED = 403 
#     FORBIDDEN  =404
#     INTERVAL_SERVER = 500

# def check(status):
#     if status == Http.SUCCESS:
#         return "Korat hal ast"
#     elif status == Http.NOT_FOUND:
#         return "Mo in chizro naedonem"
#     elif status == Http.INTERNAL_SERVER:
#         return "Abi server"
#     else:
#         return "Hashinokhtm i chiza"

# res = check(Http.NOT_FOUND)
# print(res)



