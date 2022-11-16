# q1

# A = "a:b:c:d"
# B = A.split(":")
# C = "#".join(B)
# print(C)

# q2

# a = {'A': 90, 'B' : 80}

# try:
#     print(a['C'])
# except:
#     print(70)

# q3

# a = [1,2,3]

# a = a + [4,5]

# a = [1,2,3]
# a.extend([4,5])

# ==> 같음

# q4

# A = [20,55,67,82,45,33,90,87,100,25]
# result = 0
# for i in A:
#     if i >= 50:
#         result += i
# print(result)

# q5

# def Fibo(n):
#     list = [0,1]
#     if n <= 1:
#         print(list)
#     else:
#         while list[-1] + list[-2] <= n:
#             new = list[-1] + list[-2]
#             list.append(new)
#         print(list)

# Fibo(10)

# q6

# def sum(*args):
#     result = 0
#     for i in args:
#         result += i
#     print(result)
# sum(1,2,3,4,5,6,7,8,9)

# q7

# num = int(input("구구단을 출력할 숫자를 입력하세요(2~9) : "))
# for i in range(1,10):
#     print(num * i, end=" ")

# q8

# f = open("py/abc.txt", "r")
# txt = f.read().split("\n")
# txt.reverse()
# txt = "\n".join(txt)
# print(txt)
# f.close()

# f = open("py/abc.txt", "w")
# f.write(txt)
# f.close()

# q9

# f = open("py/sample.txt", "r")
# val = f.read().split("\n")
# sum = 0
# f.close()

# for i in val:
#     sum += int(i)
# avg = sum/len(val)

# f = open("py/result.txt", "w")
# f.write(str(avg))
# f.close()

# q10

# class Calculator:
#     def __init__(self,list) -> None:
#         self.list = list
#     def sum(self):
#         result = 0
#         for i in self.list:
#             result += i
#         return result
#     def avg(self):
#         result = 0
#         for i in self.list:
#             result += i
#         result /= len(self.list)
#         return result

# cal1 = Calculator([1,2,3,4,5])
# print(cal1.sum())
# print(cal1.avg())

# cal2 = Calculator([6,7,8,9,10])
# print(cal2.sum())
# print(cal2.avg())

# q12


# q13

# def DashInsert(n):
#     nList = list(n)
#     print(nList)
#     resList = []
#     i = 0
#     while True:
#         resList.append(nList[i])
#         if i == len(nList) - 1:
#             break
#         if int(nList[i]) % 2 == 0 and int(nList[i + 1]) % 2 == 0:
#             resList.append("*")
#         elif int(nList[i]) % 2 == 1 and int(nList[i + 1]) % 2 == 1:
#             resList.append("-")
#         i += 1
#     return "".join(resList)

# print(DashInsert("4546793"))

# q14

# def zip(s):
#     sList = list(s)
#     resList = []
#     i = 0
#     while True:
#         if i > len(sList) -1:
#             break
#         cnt = 0
#         for j in sList[i:]:
#             if sList[i] == j:
#                 cnt += 1
#             else:
#                 break
#         resList.append(sList[i])
#         resList.append(str(cnt))
#         i += cnt
#     return "".join(resList)

# print(zip("abccbbbddddddddaaabbd"))

# q15

# def dup(n):
#     setN = set(n)
#     listN = list(n)
#     if len(setN) == 10 and len(listN) == 10:
#         return True
#     else:
#         return False


# print(dup("1234"))
# print(dup("1234567890"))
# print(dup("1234567890123"))
# print(dup("1973826450"))

# q16

# mos = {
#     "A" : ".-",
#     "B" : "-...",
#     "C" : "-.-.",
#     "D" : "-..",
#     "E" : ".",
#     "F" : "..-.",
#     "G" : "--.",
#     "H" : "....",
#     "I" : "..",
#     "J" : ".---",
#     "K" : "-.-",
#     "L" : ".-..",
#     "M" : "--",
#     "N" : "-.",
#     "O" : "---",
#     "P" : ".--.",
#     "Q" : "--.-",
#     "R" : ".-.",
#     "S" : "...",
#     "T" : "-",
#     "U" : "..-",
#     "V" : "...-",
#     "W" : ".--",
#     "X" : "-..-",
#     "Y" : "-.--",
#     "Z" : "--..",
#     " " : "  "   
# }
# str = ".... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--  --.. --.."

# list = str.split(" ")
# print(list)
# result = []
# for i in list:
#     key = ""
#     try:
#         key = [k for k,v in mos.items() if v == i][0]
#     except:
#         key = " "
#     result.append(key)

# print("".join(result))

