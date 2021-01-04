# 생성자(Constructor)
"""
생성자는 클래스의 인스턴스를 생성할 때 무조건 실행되는 함수이다
def __init__() 하여 만든다
init은 영어 초기 내용을 설정하다 라는 뜻을 가진 initialize의 약자입니다
"""
class FourCal():
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
    def add(self):
        result = self.first + self.second
        return result
    
    def sub(self):
        result = self.first - self.second
        return result
    
    def mul(self):
        result = self.first * self.second
        return result
    
    def div(self):
        result = self.first / self.second
        return result
a = FourCal(4, 2) # 인스턴스를 생성할 때, __init__함수가 자동으로 실행되기 때문에 바로 인자를 넣어 인스턴스 변수를 선언해주었다.
print(a.add())

# 상속(Inheritance)
"""
상속은 다른 코드를 가져와 사용할 수 있게 해주는 것이다
파이썬에서는 클래스 상속을 지원하고 있는데, 클래스 상속은 다른 클래스의 코드를 가져와 사용할 수 있게 해준다
class 클래스이름(상속할 클래스 이름): 하여 사용한다
"""

class ExpendCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

a = ExpendCal(5, 2)
print(a.pow())

"""
상속받은 클래스에서는 매서드(클래스 안에 있는 함수)를 수정하여 사용할 수 있다
상속한 클래스에 있는 매서드 이름을 그래도 쓰면 수정하여 사용할 수 있는데, 이를 메서드 오버라이딩(Overriding)이라고 한다
"""
class ZeroDivCal(FourCal):
    def div(self):
        if self.second == 0:
            result = 0
            return result
        else:
            result = self.first / self.second
            return result
a = ZeroDivCal(4, 0)
print(a.div())