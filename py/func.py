# def a(a,b):
#     max = a
#     y = b
#     for i in range(1,max):
#         x = y
#         if i < max/2:
#             for j in range(1,i):
#                 x = x + y
#         else :
#             for j in range(1,max-i):
#                 x = x + y
#         if i % 2 == 1 :
#             print(f"{x:0^{max}}")
# while True:
#     try:
#         x = str(input("문자 입력 :"))
#         y = int(input("숫자 입력 :"))
#         if len(x) == 1:
#             if x == "0" or y == 0:
#                 print("종료")
#                 break
#             a(y,x)
#         else:
#             print("문자는 1개만 입력하세요.")
#     except:
#         print("error")

# a = 1
# b = 2
# def plusOne(a):
#     return a + 1

# a = plusOne(a)
# b = plusOne(b)
# print(a)
# print(b)

# plusOne = lambda a: a+1

# a = plusOne(a)
# b = plusOne(b)
# print(a)
# print(b)

# def plusOneA():
#     global a
#     a = a + 1

# plusOneA()
# print(a)

# for i in range(10):
#     print(i,end=".")

# def is_odd(number):
#     if number % 2 == 1:
#         return True
#     else:
#         return False

# print(is_odd(3))

# def avg_numbers(*args):
#     result = 0
#     for i in args:
#         result += i
#     return result/len(args)
# print(avg_numbers(1,2))
# print(avg_numbers(1,2,3,4,5))


