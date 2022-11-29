# 251.py
# 클래스: 객체나 인스턴스의 설계도(붕어빵 틀)
# 객체: object
# 인스턴스

# 252.py
class Human:
    pass

# 253.py
class Human: # Class
    pass

areum = Human() # 객체 Binding

# 254.py
class Human:
    def __init__(self): # 생성자: 자동으로 호출되는 함수
        print("응애응애")

areum = Human() # 객체 생성 시, 생성자 자동 호출

# 255.py
class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

areum = Human("률", 22, "여자")

# 256.py
print(areum.name)
print(areum.age)
print(areum.gender)

# 257.py
class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def who(self): # self로 객체를 binding
        print(f"이름: {self.name} 나이: {self.age} 성별: {self.gender} ")

areum = Human("세희", 22, "남자")
areum.who() # Human.who(areum)

# 258.py
class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def who(self):
        print(f"이름: {self.name} 나이: {self.age} 성별: {self.gender} ")
    
    def setInfo(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
areum = Human("불명", "미상", "모름")
areum.who() # Human.who(areum)

areum.setInfo("호윤", 22, "남자")
areum.who()

# 259.py
class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 소멸자
    def __del__(self):
        print("나의 죽음을 알리지마라")

    def who(self):
        print(f"이름: {self.name} 나이: {self.age} 성별: {self.gender} ")
    
    def setInfo(self, name, age, gender): 
        self.name = name
        self.age = age
        self.gender = gender

areum = Human("수림", 22, "여자")
del(areum) # 소멸자

# 260.py
class OMG :
    def print() : # -> def print(self) 
        print("Oh my god")


mystock = OMG()
mystock.print() # OMG.print(mystock)