# class Calculator:

#     def __init__(self) -> None: # constructor , ()-> None : void => return type
#         self.result = 0

#     def plus(self,num):
#         self.result+=num
#         return self.result

#     def minus(self,num):
#         self.result-=num
#         return self.result
    
#     def multi(self,num):
#         self.result*=num
#         return self.result

#     def divi(self,num):
#         self.result/=num
#         return self.result
# cal1 = Calculator()
# cal2 = Calculator()

# print(cal1.plus(10))
# print(cal1.plus(10))
# print(cal1.minus(5))
# print(cal1.multi(6))
# print(cal1.divi(2))
# print(cal2.plus(20))
# print(cal2.plus(20))


class FourCal:
    def __init__(self,first,second) -> None:
        self.first = first
        self.second = second
    
    def setdata(self,first,second):
        self.first = first
        self.second = second
    
    def plus(self):
        result = self.first + self.second
        return result
    def minus(self):
        result = self.first - self.second
        return result
    def multi(self):
        result = self.first * self.second
        return result
    def divi(self):
        result = self.first / self.second
        return result

# fCal = FourCal()  # not exist constructor
# fCal.setdata(10,2)
# print(fCal.plus())
# print(fCal.minus())
# print(fCal.multi())
# print(fCal.divi())

# fCal2 = FourCal(20,4)
# print(fCal2.plus())
# print(fCal2.minus())
# print(fCal2.multi())
# print(fCal2.divi())
# fCal2.setdata(10,2)
# print(fCal2.plus())
# print(fCal2.minus())
# print(fCal2.multi())
# print(fCal2.divi())

# class SafeFourCal(FourCal):
#     def divi(self):
#         if self.second == 0:
#             return 0
#         else:
#             return self.first / self.second
#     def pow(self):
#         result = self.first ** self.second
#         return result

# sFCal = SafeFourCal(5,3)
# print(sFCal.pow())
# sFCal.setdata(5,0)
# print(sFCal.pow())
# print(sFCal.divi())

# class A:
#     a = 1

# B = A()
# C = A()
# B.a = 2
# C.a = 3
# print(A.a)
# print(B.a)
# print(C.a)

# B = A()
# C = A()
# A.a = 4
# print(A.a)
# print(B.a)
# print(C.a)

# class Calculator:
#     def __init__(self) -> None:
#         self.value = 0
    
#     def add(self,val):
#         self.value += val

# class UpgradeCalculator(Calculator):
#     def minus(self,val):
#         self.value -= val

# cal = UpgradeCalculator()
# cal.add(10)
# cal.minus(7)

# print(cal.value)

# class MaxLimitCalculator(Calculator):
#     def add(self,val):
#         self.value += val
#         if self.value > 100:
#             self.value = 100

# cal = MaxLimitCalculator()
# cal.add(50)
# cal.add(60)

# print(cal.value)