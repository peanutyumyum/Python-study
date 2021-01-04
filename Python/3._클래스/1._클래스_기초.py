# 클래스
"""
클래스는 코드 덩어리다
클래스의 인스턴스는 하나의 객체가 된다
클래스 안에 선언되는 변수는 인스턴스변수라고 부르고 클래스 변수와 객체 변수로 나뉜다
클래스 변수는 클래스의 모든 인스턴스에서 공통적으로 적용되는 것이고
객체변수는 클래스의 인스턴스 중 객체에 따라 변하는 변수이다.(물론 객체변수는 어느 곳에서든 접근 가능하고 사용가능하긴 하다)

객체변수를 선언하고 싶으면 self를 사용해야 한다
self를 사용하므로서 하나하나의 객체를 조금 더 독립적으로 운용할 수 있게 되는 것이다
self를 사용하게 되면 객체.변수이름 하여 객체변수에 접근할 수 있게 된다
참고로 self는 관례적으로 사용되는 것이다
"""

class FourCal():
    def setdata(self, first, second):
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

a = FourCal() # 클래스의 인스턴스를 생성해주고
a.setdata(4, 2) #객체.함수이름 하여 객체 안에 있는 인스턴스 변수를 선언해준다
print(a.add()) # 객체.함수이름 하여 함수 실행