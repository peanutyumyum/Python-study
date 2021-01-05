# try와 except문(오류 예외 처리)
"""
try문은 사용하면 try문 안에서 오류가 발생하면 오류를 발생시키는 것이 아니라 except블록을 실행시킨다

try문은 다음과 같은 구조를 가진다
try:
    실행할 코드
except [발생오류들[as e]]:
    오류가 발생할 때 실행할 코드
else:
    오류가 발생하지 않을 때 실행할 코드

참고로 []는 관례적으로 사용되는 것으로 생략해도 무방하다
발생오류를 복수로 지정하고 싶은 경우 ()로 괄호로 묶어 사용한다
또 e는 except의 약자로 파이썬에 저장되어 있는 오류발생 메시지 변수이다 e를 사용하면 오류가 발생하면 오류 메시지(오류 이유)가 나온다

1. tyr문에서 except문은 발생오류를 특정하지 않아도 상관 없다 이렇게 할 경우 모든 오류에 대해서 except문을 실행시킨다
2. try문에서 except문은 발생오류만 쓰고 e(오류메시지 변수)를사용하지 않을 수도 있다 이럴경우 오류메시지는 볼 수 없다
3. try문에서 except문은 발생오류와 e를 모두 사옹해 쓸 수 있다

참고로 except문의 발생오류를 적을 때 모든 발생오류에 대해서 처리하고 싶으면 Exception을 사용하면 된다

"""

try:
    print(4 / 0)
except:
    print("0으로는 나눌 수 없습니다")

try:
    print(4 / 0)
except ZeroDivisionError:
    print("0으로는 나눌 수 없습니다")

try:
    print(4 / 0)
except ZeroDivisionError as e:
    print("0으로는 나눌 수 없습니다", e)

try:
    print(4 / 0)
except Exception as e:
    print("0으로는 나눌 수 없습니다", e)

"""
발생오류를 복수로 지정하고 싶은 경우 ()로 괄호로 묶어 사용한다
"""
try:
    print(4 / 0)
except (ZeroDivisionError, IndexError) as e:
    print("0으로는 나눌 수 없습니다", e)


# finally
"""
finally는 try문에서 except문이 실행되더라도 상관 없이 실행되는 코드이다

try:
    실행할 코드
finally:
    except실행 여부와 관계없이 사용할 코드
except [발생오류[as e]]:
    오류가 발생할 때 실행할 코드
else:
    오류가 발생하지 않을 때 실행할 코드

이런 구조로 사용되며, 보통 리소스를 close해야할 때 사용된다
"""
try:
    print(4 / 0)
except Exception as e:
    print("0으로는 나눌 수 없습니다", e)
finally:
    print("저는 항상 수행됩니다")

# pass
"""
except문에 pass를 아무 코드도 실행하지 않기 때문에 사용하면 오류를 회피할 수 있다
"""
try:
    print(4 / 0)
except ZeroDivisionError:
    pass

# raise
"""
raise는 오류를 일으킨다
일부러 오류를 일으키고 싶을 때 사용하면 된다
raise 오류이름 으로 만들면 된다
"""

raise NotImplementedError