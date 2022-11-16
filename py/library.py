# import sys

# print(sys.argv)

# sys.exit()

# import pickle

# f = open("py/test.txt", "wb")
# data = {1: "python", 2: "you need", 3: "!"}
# pickle.dump(data, f)
# f.close()

# f = open("py/test.txt","rb")
# data = pickle.load(f)
# print(data)

# import os
# import pickle

# print(os.environ)
# print(os.getcwd())
# os.chdir(f"{os.getcwd()}/py") #change directory 실행 중인 동안에만 적용

# f = open("test.txt","rb")
# data = pickle.load(f)
# print(data)

# print(os.getcwd())

# print(os.system("dir"))

# f = os.popen("dir")
# print(f.read())

# import shutil

# shutil.copy("py/hi.txt", "py/hi2.txt")

# import glob
# import os

# print(glob.glob(f"{os.getcwd()}/py/hi*"))

# import tempfile
# filename = tempfile.mkstemp()
# print(filename)
# f = tempfile.TemporaryFile()
# f.close()

# import time
# print(time.asctime(time.localtime(time.time())))
# print(time.ctime())
# print(time.strftime("%x", time.localtime()))

# import calendar
# print(calendar.calendar(2022))
# print(calendar.prmonth(2022, 11))

import webbrowser
webbrowser.open("https://www.naver.com")