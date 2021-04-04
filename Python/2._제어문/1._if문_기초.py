# if문은 참이 되면 실행된다.

if True:
    print("참입니다.")

# else
"""
else는 위의 조건이 모두 거짓이었을 때 실행된다.
"""

if False:
    print("참입니다.")
else:
    print("거짓입니다.")

# elif
"""
elif는 이전 조건이 거짓일 때, 본 조건문이 참이면 실행된다.
또 갯수에 제한이 없어서 여러번 사용될 수 있다.
"""
if False:
    print("실행안되겠죠")
elif True:
    print("실행됩니다")
elif True:
    print("그리고 저는 갯수에 제한이 없습니다.")
else:
    print("위에서 실행됐기 때문에 실행되지 않습니다.")

if 1 != 2: # 비교연산자를 사용하여 if문을 만들었다. != 은 다르다는 뜻이다.
    print("둘은 다릅니다.")
else:
    print("둘은 같습니다.")

# 비교연산자
"""
x or y - 둘 중 하나만 참이어도 참이다(또는, 혹은)
x and y - 둘 다 참이어야 참이다(그리고)
not x - x가 거짓이면 참이다(참 거짓을 바꿔줌)
"""
if not False:
    print("거짓을 입력했는데 실행되었다면, 분명 not을 사용했군요!")


# in과 not in
"""
x in 리스트, 튜플, 문자열 - 리스트, 튜플, 문자열에 x가 있는가?
x not in 리스트, 튜플, 문자열 - 리스트, 튜플, 문자열에 x가 없는가?
"""
if 1 not in [2, 3, 4]:
    print("리스트에는 1이 없군요!")

# pass
"""
pass는 아무 효과가 없는 제어문으로, 보통 제어문 혹은 class에 내용을 넣지 않은 상태에서 틀만 만들어 놓고 싶을 때 사용한다
pass를 사용하면 안에 유의미한 코드는 없지만, 오류가 나지 않기 때문이다
"""
if True:
    pass

# 조건부 표현식
score = int(input("점수를 입력하세요"))
if score >= 60:
    message = "성공"
else:
    message = "실패"
print(message)
"""
이와 같은 표현을 한줄로 사용할 수 있다.
"""
message = "성공" if score >= 60 else "실패"
print(message)