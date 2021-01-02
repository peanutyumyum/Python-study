# 함수
"""
함수는 호출하여 사용할 수 있고, 실행하면 일정한 코드를 수행한다.
입력값이 있을 수도 있고 없을 수도 있다
또 결과값이 있을 수도 있고 없을 수도 있다
"""

def add(a, b):
    return a + b

print(add(3, 4))

"""
함수는 매개변수와 인수가 여러 개 일수도 있지만
결과값은 오직 하나이다. 다만 결과값이 여러 개의 값으로 이루어 질 수는 있다. 예를 들면 튜플로 이루어질 수 있는 것
결과값이 여러 개의 값으로 이루어질 경우에는 튜플로 생성된다
"""
def result(a, b):
    return a + b, a * b
print(result(3, 4)) #(7, 12) 출력

"""
이때, 여러가지 변수 생성 방식을 응용하면 다음과 같은 것도 가능하다
"""
a, b = result(3, 4)
"""
이러한 경우 a에 7이 저장되고, b에 12가 저장된다
"""

# 함수의 매개변수에 기본값 설정하기
"""
함수의 매개변수에 기본값을 설정할 수 있다
def 함수이름(매개변수1, 매개변수2, 매개변수3 = 기본값): 으로 설정한다
매개변수에 아무것도 입력되있지 않다면 설정한 기본 값으로 함수가 실행된다
"""
def who_you_are(name, old, gender = "man"):
    print("나의 이름은 %s 입니다" % name)
    print("나의 나이는 %d 입니다" % old)
    if gender == "man":
        print("나는 남자다")
    elif gender == "woman":
        print("나는 여자다")
who_you_are("지원", 25, "woman")

# *args
"""
입력값이 얼마나 될지 모를 때 사용한다
def 함수이름(*매개변수): 으로 사용한다
args는 영어 arguments(매개변수)의 약자이고, 관례적으로 자주 사용한다
"""

def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result
result = add_many(1, 2, 3, 4)
print(result)

"""
*args는 다른 매개변수와도 사용될 수 있다.
"""
def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 0
        for i in args:
            result = result * i
    return result
result = add_mul("mul", 1, 2, 3, 4)
print(result)

# **kwargs(딕셔너리를 생성하는 함수)
"""
**kwargs는 입력한 인수를 딕셔너리로 생성해 결과값으로 반환하는 하게 한다
딕셔너리의 key는 매개변수가 되고, value는 입력한 인수가 된다
kwargs는 keyword arguments의 약자이고 관례적으로 사용된다
"""
def print_kwargs(**kwargs):
    print(kwargs)
print_kwargs(a = 3, b= "hi")

# return의 응용
"""
return은 함수에서 사용될 수도 있고 사용되지 않을 수도 있지만,
사용된다면 함수를 끝내는 역할을 하게 된다
물론 return 후에 아무것도 써주지 않으면 결과값이 없는 함수가 된다
"""
def do_return(say):
    if say == "hi":
        return
    print("what?")
do_return("hi") # hi가 입력되면 return에 도달하여 결과값이 없는 상태로 함수가 종료되는 함수

"""
기본적으로 모든 함수는 함수 밖에 있는 변수를 사용할 수 없다
마찬가지로 함수 밖에서 함수 안에 있는 변수를 사용할 수 없다
다만 global을 이용하여 함수 밖에 있는 변수를 안에서 사용할 수 있게끔 할 수는 있다
"""