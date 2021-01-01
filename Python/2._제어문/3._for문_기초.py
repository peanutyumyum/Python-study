# for문
"""
for문은 리스트, 튜플, 문자열의 첫 번째 요소부터 마지막 요소까지 차례대로 변수에 대입되는 제어문이다.

예를 들면,
for 변수 in 리스트(튜플이나 문자열이 와도 무방)
    수행할 코드
와 같이 수행된다.
"""
for_list = ["one", "two", "three"]
for i in for_list:
    print(i)


# for문의 변수를 여러가지 사용하기
"""
for문의 변수로 하나만이 아니라 여러개를 이용할 수도 있다.
"""

a = [[1, 2], [3, 4], [5, 6]]
for [b, c] in a:
    print(b + c)
"이러한 경우 b에 각각 1, 3, 5가 대입되고, c에는 각각 2, 4, 6이 대입된다."

# continue(다시 되돌아가기)
"""
for문에서도 continue를 사용할 수 있다.
for문에서 continue는 무조건 for문을 다시 시작한다.
이때, 코드를 다시 시작한다는 것이지, 그 전까지 시행되었던 조건을 초기화 시키고 다시 시작한다는 뜻은 아니다.
밑에 쓰여져 있는 코드는 실행되지 않고 무조건 for문을 처음 시작한다.
"""

score = [90,25, 67, 45, 80]
number = 0
for student in score:
    number += 1
    if student < 60:
        continue
    else:
        print("%d번 학생은 합격입니다." % number)

# range함수를 이용한 for문
"""
for문은 range함수와 같이 자주 사용된다.

range함수란?
range 함수는 range(시작숫자, 끝숫자, 얼마씩 증가할 것인지)로 이루어지며, 
시작숫자부터 끝 숫자 직전까지의 범위에 있는 숫자를 값으로 반환해주는 함수이다. 
이때 설정해놓은대로 증가하여 끝 숫자에 도달하기 전까지 진행되며, 얼마씩 증가할지에 대해 정하지 않으면 기본값은 1이다.
"""
sum = 0
for counts in range(0, 10, 1):
    sum = sum + counts
print(counts)