class SelfTest:
    def __init__(self):
        print("생성자 호출시 self 변수에 전달되는 값 :", self)
    def m1(self):
        print("m1() 호출시 self 변수에 전달되는 값 :", self)
    def m2(self):
        print("m2() 호출시 self 변수에 전달되는 값 :", self)
    def __str__(self):   # 객체를 문자열로 변환할 때 호출되는 특수메서드
        return "***객체 정보를 문자열로 표현***"

obj1 = SelfTest()
print("obj1이 참조하는 객체 : "+str(obj1))
obj1.m1()
obj1.m2()
print("-"*70)
obj2 = SelfTest()
print("obj1이 참조하는 객체 : "+str(obj2))
obj2.m1()
obj2.m2()

