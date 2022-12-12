# Q1
# 홍길동 = {
#     "국어" : 80,
#     "영어" : 75,
#     "수학" : 55
# }

# 총합 = 홍길동["국어"] + 홍길동["영어"] + 홍길동["수학"]
# 평균 = 총합/len(홍길동)
# print(평균)

# Q2
# n = 13
# if n % 2 == 0:
#     print(f"{n} : 짝수")
# else:
#     print(f"{n} : 홀수")

# Q3
# pin = "881120-1068234"
# yyyymmdd = pin[:6]
# num = pin[7:]
# tt = 0
# if int(num[0]) < 3:
#     tt = 19
# else:
#     tt = 20
# print(f"{tt}{yyyymmdd}")
# print(num)

# Q4
# pin = "881120-1068234"
# print(pin[7])

# Q5
# a = "a:b:c:d"
# b = a.replace(":","#")
# print(b)

# Q6
# a = [1,3,5,4,2]
# a.sort()
# a.reverse()
# print(a)

# Q7
# a = ['Life', 'is', 'too', 'short']
# result = ' '.join(a)
# print(result)

# Q8
# a = (1,2,3)
# a = a + (4,)
# print(a)

# Q9
# a = dict()
# a['name'] = 'python'
# a[('a',)] = 'python'
# a[[1]] = 'python'  # key 값은 contant 해야함
# a[250] = 'python'

# Q10
# a = {'A' : 90, 'B' : 80, 'C' : 70}
# result = a.pop('B')
# print(a)
# print(result)

# Q11
# a = [1,1,1,2,2,3,3,3,4,4,5]
# aSet = set(a)
# b = list(aSet)
# print(b)

# Q12
# a = b = [1,2,3]
# a[1] = 4
# print(b)
# => b 가 a 와 같은 주소를 가짐 a 가 바뀌면 b 도 바뀜

###################################################

# Q1
# a = "Life is too short, you need python"
# if "wife" in a: print("wife")
# elif "python" in a and "you" not in a: print("python")
# elif "shirt" not in a: print("shirt")
# elif "need" in a: print("need")
# else: print("none")

# Q2
# result = 0
# i = 1
# while i <= 1000:
#     if i % 3 == 0:
#         result += i
#     i += 1

# print(result)

# Q3
# i = 0
# while True:
#     i += 1
#     if i > 5: break
#     print("*"*i)

# Q4
# for i in range(1,101):
#     print(i)

# Q5
# A = [70,60,55,75,95,90,80,80,85,100]
# total = 0
# for score in A:
#     total += score
# average = total / len(A)
# print(average)

# Q6
# numbers = [1,2,3,4,5]

# result = []
# for n in numbers:
#     if n % 2 == 1:
#         result.append(n*2)
# print(result)

# result2 = [n*2 for n in numbers if n % 2 == 1]
# print(result2)

#######################################################

# Q1
# def is_odd(number):
#     if number % 2 == 1:
#         return True
#     else:
#         return False

# Q2
# def avg_numbers(*args):
#     result = 0
#     for i in args:
#         result += i
#     return result/len(args)
# print(avg_numbers(1,2))
# print(avg_numbers(1,2,3,4,5))

# Q3
# input1 = int(input("첫번째 숫자 : "))
# input2 = int(input("두번째 숫자 : "))

# total = input1 + input2
# print(f"두 수의 합 : {total}")

# Q4
# print("hi","bye") # 사이에 공백추가

# Q5
# f1 = open("test.txt", 'w')
# f1.write("Life is too short")
# f1.close()

# f2 = open("test.txt", 'r')
# print(f2.read())
# f2.close()

# Q6
# user_input = input("저장할 내용 : ")
# f = open("test.txt", 'a')
# f.write(user_input)
# f.write("\n")
# f.close()

# Q7
# f = open('test.txt', 'r')
# body = f.read()
# f.close()
# body = body.replace("java", "python")

# f = open('test.txt', 'w')
# f.write(body)
# f.close()

#####################################################

# Q1
# class Calculator:
#     def __init__(self) -> None:
#         self.value = 0
#     def add(self, val):
#         self.value += val

# class UpgradeCalculator(Calculator):
#     def minus(self,val):
#         self.value -= val

# cal = UpgradeCalculator()
# cal.add(10)
# cal.minus(7)
# print(cal.value)

# Q2
# class Calculator:
#     def __init__(self) -> None:
#         self.value = 0
#     def add(self, val):
#         self.value += val
# class MaxLimitCalculator(Calculator):
#     def add(self, val):
#         self.value += val
#         if self.value > 100:
#             self.value = 100
    
# cal = MaxLimitCalculator()
# cal.add(50)
# cal.add(60)
# print(cal.value)

# Q3
# print(all([1,2,abs(-3)-3]))
# print(chr(ord('a')) == 'a')

# Q4
# a = [1,-2,3,-5,8,-3]
# print(list(filter(lambda x: x > 0, a)))

# Q5
# hx = hex(234)
# print(hx)
# num = int(hx,16)
# print(num)

# Q6
# a = [1,2,3,4]
# print(list(map(lambda x: x*3, a)))

# Q7
# a = [-8,2,7,5,-3,5,0,1]
# print(max(a)+min(a))

# Q8
# print(round(17/3,4))

# Q9
# import sys