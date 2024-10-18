# import asyncio 

# async def say_hello():
#     print("Salom")
#     await asyncio.sleep(2)
#     print("khay")
    
# asyncio.run(say_hello())


# 2
# import asyncio 

# async def say_hello():
#     print("Salom")
#     await asyncio.sleep(3)
#     print("Task Complated")
    
# asyncio.run(say_hello())



# 3
# a = int(input("-> "))
# b = 1
# cnt2 = 0
# while b<=a:
#     if b%2==0:
#         cnt2-=b
#     else:
#         cnt2+=b
#     b+=1

# print(cnt2)
        
        
# 4
# a = int(input("-> "))

# cnt = 0

# for i in range(1,a):
#     if a % i==0:
#         cnt = i
        
# if cnt < 2:
#     print("prime")
# else:
#     print("not prime")


# 5
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# i = 0
# while i < len(a):
#     cnt = a[i]
#     if cnt < 2:
#         del a[i]
#         continue
#     cnt1 = 2
#     cnt3 = 0  
#     while cnt1 * cnt1 <= cnt:
#         if cnt % cnt1 == 0:
#             cnt3 = 1
#             break
#         cnt1 += 1
#     if cnt3 == 1:
#         del a[i]
#     else:
#         i += 1
# print(a)


# 6

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# cnt1 = {}
# for i in a:
#     cnt = 0
#     for f in range(1, i + 1):
#         if i % f == 0:
#             cnt += 1
#     cnt1[i] = cnt

# print(cnt1)


# 8
# def main(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return main(n - 1) + main(n - 2)

# print(main(int(input("-> "))))

# 9
# def main(a):
#     def innner(n):
#         return n * a
#     return innner

# cnt = main(5)


# print(cnt(10))  
# print(cnt(3))   
# print(cnt(7))   




