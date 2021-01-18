# 데코레이타(Decorator)
"""
함수를 장식하는 역할을 하는 것

@받을 함수 이름
def 함수이름():
하여 사용한다

데코레이터는 함수를 수정하지 않은 상태에서 추가 기능을 구현할 때 사용한다
개념은 서로 다르지만, 클래스의 상속기능을 모방한 것이라고 봐도 무방하다
"""
def decorator(func):
    def wrapper():
        print(func.__name__, '함수 시작')
        func()
        print(func.__name__, '함수 끝')
    return wrapper
 

@decorator
def hello():
    print('함수 실행')

hello()
"""
func를 매개변수로 사용하면, 함수를 인자로 받을 수 있다(일급 객체의 개념 이용)
"""