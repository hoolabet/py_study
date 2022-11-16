import random
from re import I

# s = set()
# while len(s) != 6:
#     s.add(random.randrange(1,46))
# li = list(s)
# li.sort()
# print(li)

# li = list(range(1,46))
# res = list()
# while len(res) != 6:
#     random.shuffle(li)
#     res.append(li.pop())
# res.sort()
# print(res)

# result = 0
# i = 1
# while i <=1000:
#     if i % 3 ==0:
#         result += i
#     i += 1
# print(result)

# i=0
# while True:
#     i += 1
#     if i > 5:break
#     print("*" * i)

# for i in range(1,101):
#     print(i)

# A = [70,60,55,75,95,90,80,80,85,100]
# total = 0
# for score in A:
#     total += score
# average = total/len(A)
# print(average)

numbers = [1,2,3,4,5]
result = [n*2 for n in numbers]
print(result)

