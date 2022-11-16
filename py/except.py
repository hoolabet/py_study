# a = 1
# b = "2"
# # b = 2
# try:
#     c = a + b
# except Exception:
#     import traceback
#     traceback.print_exc()
# else:
#     print(f"a + b = {c}")
# finally:
#     print("hi")

# class MyError(Exception):
#     def __str__(self) -> str:
#         return "ㅋㅋㅋ"

# def say_nick(nick):
#     if nick == "ㅋ":
#         raise MyError()
#     print(nick)
# while True:
#     try:
#         str = input("닉네임을 입력하세요 : ")
#         say_nick(str)
#     except MyError as e:
#         print(e)
#         break

a = (1,10,100)

for i,v in enumerate(a):
    print(i, v)