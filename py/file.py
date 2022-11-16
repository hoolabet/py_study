# f = open("D:/01-STUDY/vs/py/hi.txt","w")
# for i in range(1,11):
#     data = f"{i}\n"
#     f.write(data)
# f.close()

# f = open("D:/01-STUDY/vs/py/hi.txt","r")

# while True:
#     line = f.readline()
#     if not line:break
#     print(line)

# for line in lines:
#     print(line)

# data = f.read()
# print(data)

# f.close()

# import os


# f = open("D:/01-STUDY/vs/py/hi.py","w")
# data = "a = 1"
# f.write(data)
# f = open("D:/01-STUDY/vs/py/hi.py","r")
# data = f.read()
# print(data)
# f.close()
# os.remove("D:/01-STUDY/vs/py/hi.py")


# f = open("D:/01-STUDY/vs/py/hi.txt","r")

# cnt = len(f.readlines())

# f = open("D:/01-STUDY/vs/py/hi.txt","a")

# for i in range(cnt+1,cnt+11):
#     data = f"{i}\n"
#     f.write(data)
# f.close()

# f1 = open("D:/01-STUDY/vs/py/test.txt","w")
# f1.write("Life is too short")
# f1.close()

# f2 = open("D:/01-STUDY/vs/py/test.txt","r")
# print(f2.read())
# f2.close()

# user_input = input("저장할 내용을 입력하세요 : ")
# f = open("D:/01-STUDY/vs/py/test.txt","a")
# f.write(user_input+"\n")
# f.close()

# f = open("D:/01-STUDY/vs/py/test.txt","r")

# body = f.read()
# f.close()

# body = body.replace("java","python")

# f = open("D:/01-STUDY/vs/py/test.txt","w")
# f.write(body)
# f.close()

# with open("D:/01-STUDY/vs/py/test.txt","r") as f:
#     print(f.read())


dic = {"a": 1, "b": 2}

print(dic)

dic = dict((v,k) for k,v in dic.items())

print(dic)