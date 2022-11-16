import re

# p = re.compile("[a-c]")

# print(p.match("a"))
# print(p.match("A"))
# print(p.match("d"))

# print(p.search("a"))
# print(p.search("zzdecab"))

# print(p.findall("1a2b3c"))
# for r in p.finditer("1a2a3a4b5b6b7c8c9c"):
#     print(r)

# p = re.compile("a.c")
# print(f"""a.c => match(abc) : {p.match("abc")}""")
# print(f"""a.c => match(adc) : {p.match("adc")}""")
# print(f"""a.c => match(ac) : {p.match("ac")}""")
# print(f"""a.c => match(a123c) : {p.match("a123c")}""")
# p = re.compile("a...c")
# print(f"""a...c => match(a123c) : {p.match("a123c")}""")
# p = re.compile("a[.]c")
# print(f"""a[.]c => match(abc) : {p.match("abc")} """)
# print(f"""a[.]c => match(a.c) : {p.match("a.c")} """)
# p = re.compile("a[!]c")
# print(f"""a[!]c => match(a!c) : {p.match("a!c")} """)

# p = re.compile("hi|hello")
# m = p.match("hiha")
# print(m)
# m = p.match("hahi")
# print(m)
# m = p.match("hi zz")
# print(m)
# m = p.match("hi hello")
# print(m)
# m = p.match("hello hi")
# print(m)

# print(re.search("^hi","hi bye"))
# print(re.search("^hi","bye hi"))
# print(re.search("bye$","hi bye"))
# print(re.search("bye$","bye hi"))

# data = """Life is too short
# 1Life is too short2
# Life is too short"""
# p = re.compile("Life",re.MULTILINE)
# print(p.findall(data))
# p = re.compile("^Life",re.MULTILINE)
# print(p.findall(data))
# p = re.compile("short",re.MULTILINE)
# print(p.findall(data))
# p = re.compile("short$",re.MULTILINE)
# print(p.findall(data))

# p = re.compile("\ALife",re.MULTILINE)
# print(p.findall(data))
# p = re.compile("short\Z",re.MULTILINE)
# print(p.findall(data))

#^,$ : MULTILINE 시 각 줄마다 매치 // \A,\Z : MULTILINE 시 전체 문자열에 매치

# p = re.compile(r"\bhi\b")
# print(p.search("zzz hi bye zz"))
# print(p.search("zzzhibyezz"))

# p = re.compile(r"\Bhi\B")
# print(p.search("zzz hi bye zz"))
# print(p.search("zzzhibyezz"))


# p = re.compile("(ha)+")
# m = p.search("z hahahahahahahahahaha zz haha")
# print(m)
# print(m.group(0))

# p = re.compile(r"(\b\w+)\s+\1")
# m = p.search("hi ha ha bye")
# print(m.group())
# p = re.compile(r"(?P<name>\b\w+)\s+(?P=name)")
# m = p.search("hi ha ha bye")
# print(m.group())

# p = re.compile(r"(?P<name>\w+)\s+(?P<number>(?P<local>\d+)[-]\d+[-]\d+)")
# m = p.search("hi 123-456-789")
# print(m.group("name"))
# print(m.group("number"))
# print(m.group("local"))

# p = re.compile(".+(?=:)")
# m = p.search("https://www.naver.com")
# print(m.group())

# p = re.compile(".+(?!:)")
# m = p.search("https://www.naver.com")
# print(m.group())

# p = re.compile("(hi|bye)")
# s = p.sub("zz","hi hello bye hibye")
# print(s)

# s = p.sub("zz","hi hello bye hibye", 3)
# print(s)

# s = p.subn("zz","hi hello bye hibye")
# print(s)

# p = re.compile(r"(?P<name>\w+)\s+(?P<number>(?P<local>\d+)[-]\d+[-]\d+)")
# s = p.sub("\g<number> zz \g<name>", "hi 123-456-789")
# print(s)
# s = p.sub("\g<2> zz \g<1>", "hi 123-456-789")
# print(s)

def hexrepl(match):
    value = int(match.group())
    return hex(value)

p = re.compile(r"\d+")
print(p.sub(hexrepl, "hi 1234 , bye 5678 16 32 48 160"))
