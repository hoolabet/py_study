# def GuGu(n):
#     result = []
#     for i in range(1,10):
#         result.append(n * i)
#     return result

# while True:
#     try:
#         inputN = int(input("숫자를 입력하세요. /// 종료 : 0 \n "))
#         if inputN == 0:
#             print("종료")
#             break
#         print(GuGu(inputN))
#     except:
#         print("정수인 숫자를 입력하세요.")

# def tf(n):
#     result = 0
#     if n < 0 or n >= 1000:
#         print("1에서 999 사이의 자연수만 입력하세요.")
#     else:
#         for i in range(1,n+1):
#             if i % 3 == 0 or i % 5 == 0 :
#                 result += i
#     return result

# while True:
#     try:
#         inputN = int(input("1~999 사이의 자연수를 입력하세요. /// 종료 : 0 \n"))
#         if inputN == 0:
#             print("종료")
#             break
#         print(tf(inputN))
#     except:
#         print("1에서 999 사이의 자연수만 입력하세요.")

# def getTotalPage(m,n):
#     try:
#         if m < 0 or n < 0 :
#             return 0
#         else:
#             if m % n == 0:
#                 return m / n
#             else:
#                 return m//n +1
#     except:
#         print("한 페이지당 게시물 수는 0이 될 수 없습니다.")
#         return 0

# while True:
#     try:
#         inputM = int(input("총 건수를 입력하세요. : (종료 : 0)"))
#         inputN = int(input("한 페이지당 게시물 수를 입력하세요. : "))
#         if inputM == 0:
#             print("종료")
#             break
#         print(getTotalPage(inputM,inputN))
#     except:
#         print("정수인 숫자만 입력가능합니다.")

# import sys

# option = sys.argv[1]
# if option == "-a":
#     memo = sys.argv[2]
#     f = open("py/hi.txt", "a")
#     f.write(memo)
#     f.write("\n")
#     f.close()
# elif option == "-v":
#     f = open("py/hi.txt")
#     memo = f.read()
#     f.close()
#     print(memo)

import os

# def search(dirname,extStr):
#     try:
#         filenames = os.listdir(dirname)
#         for filename in filenames:
#             full_filename = os.path.join(dirname, filename)
#             if os.path.isdir(full_filename):
#                 search(full_filename,extStr)
#             else:
#                 ext = os.path.splitext(full_filename)[-1]
#                 if ext == f".{extStr}":    
#                     print(full_filename)
#     except PermissionError:
#         pass    

# search("D:\\01-STUDY\\","css")

def search(dirname,extStr):
    try:
        for (path, dir, files) in os.walk(dirname):
            for filename in files:
                ext = os.path.splitext(filename)[-1]
                if ext == f".{extStr}":
                    print(f"{path}\\{filename}")
    except PermissionError:
        pass
search("D:\\01-STUDY\\","exe")
# search("C:\\","txt")