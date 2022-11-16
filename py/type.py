# 홍길동 = {"국어": 80, "영어" : 75, "과학" : 55, "수학" : 30}

# 총점 = 0

# for 과목 in 홍길동.keys():
#     총점 += 홍길동[과목]

# 과목수 = len(홍길동)

# 평균 = 총점 / 과목수

# 점수 = list(홍길동.values())

# 점수.sort()

# 최저점 = {"과목": [k for k,v in 홍길동.items() if v == 점수[0]][0] , "점수" : 점수[0]}
# 최고점 = {"과목": [k for k,v in 홍길동.items() if v == 점수[-1]][0] , "점수" : 점수[-1]}



# # 성적표 = """
# # 과목수 : {0}
# # 총점 : {1}
# # 평균점수 : {2}
# # 최고점 : {3} {4}
# # 최저점 : {5} {6}
# # """.format(과목수,총점,평균,최고점["과목"],최고점["점수"],최저점["과목"],최저점["점수"])

# 성적표 = f"""
# 과목수 : {과목수}
# 총점 : {총점}
# 평균점수 : {평균}
# 최고점 : {최고점['과목']} {최고점['점수']}
# 최저점 : {최저점['과목']} {최저점['점수']}
# """

# print(성적표)

# a = 13
# b = a % 2
# print(b)

# print(f"{총점:=^11}")

# 주민 = "881120-1234567"
# 연월일 = 주민[:6]
# 성별 = 주민[7]

# print(f"연월일 : {연월일}")
# print(f"성별 : {성별}")

# a = "abcd"
# print(",".join(a).split(","))
# print(a.upper())
# print(a.replace("cd","ab"))
# print(a)



# li = [0,1,2,3,4,5,6,7,8,9,1,1,2,2,2,2,3,3,4,5,5,5,5,7,7,7,7,7,7,7,8,8,9,9,9,0,0]
# while True :
#     num = 0
#     calcLi = li[:]
#     x = int(input("숫자를 입력하세요. (종료:-1)"))
#     if x == -1 :
#         break
#     while True :
#         try:
#             calcLi.remove(x)
#             num = num + 1
#         except:
#             print(f"""
#             x : {x}
#             {x} 개수 : {num}""")
#             break

# while True :
#     x = int(input("숫자를 입력하세요. (종료:-1)"))
#     if x == -1 :
#         break
#     print(li.count(x))

# x = (1,2,3)
# x = (4,) + x
# print(x*2)
# print(x)
# print(x[2:])


# a = {"a":"1","b":"2","c":"3"}

# for k,v in a.items():
#     print(f"key : {k} , value : {v}")

# print(dict((v,k) for k,v in a.items()).get("1"))

# a = "a:b:c:d"
# b = a.replace(":","#")
# print(b)

# a = [1,3,5,4,2]
# a.sort()
# a.reverse()
# print(a)

# a = ['Life','is','too','short']
# result = " ".join(a)
# print(result)

# a = (1,2,3)
# a = a + (4,)
# print(a)

# a = dict()
# a['name'] = "python"
# print(a)
# a[('a',)] = "python"
# print(a)
# # a[[1]] = "python"  key 값은 constant 만 가능
# # print(a)
# a[250] = "python"
# print(a)

# a = {'A':90,'B':80,'C':70}
# result = a.pop('B')
# print(a)
# print(result)

# name = ["hi", "hi", "bye", "hello", "bye"]
# setName = set(name)
# listName = list()
# for v in setName:
#     listName = listName + [{"name":v}]

# print(listName)

# a = set([1,2,3])
# a.add(1)
# print(a)
# a.update([3,4,5])
# print(a)

# a = [1,1,1,2,2,3,3,3,4,4,5]
# aSet = set(a)
# b = list(aSet)
# print(b)

a = b = [1,2,3] # copy() 나 [:]를 사용한것이 아니라 a와 b의 id(메모리 주소)가 같다. 
a[1] = 4
print(b)









