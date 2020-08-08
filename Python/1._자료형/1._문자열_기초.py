# 여러 줄을 가진 문자열을 변수로 지정하고 싶을 때


# 첫 번째 방법
# 이스케이프 코드 \n 사용 하기
multiple = "Life is too short\nSo you need python" # 이때 \은 /과 다르다.
print(multiple)
# 이때 이스케이프 코드는 프로그래밍 시 사용할 수 있는 미리 정의된 문자 조합을 이른다. 이스케이프 코드에는 \n을 비롯하여 \t(문자열 사이에 탭간격을 줄 때 사용), \\(\를 그대로 표현하고 싶을 때 사용), \'('를 그대로 표현하고 싶을 때 사용) 등등(더 있음)이 있다.

# 두 번째 방법
# '''(작은따음표 3개) 혹은 """(큰따음표 3개) 사용하기
multipleline_1 = """
Life is too short
So you need python
"""
print(multipleline_1)
# or

multipleline_2 = """
Life is too short
So you need python
"""
print(multipleline_2)


# 문자열의 연산


# 덧셈
a = "안녕"
b = "나는 지원이야"
print(a)
print(b)
print(a+b)

# 곱셈
a = "아"
print(a*3)


# 인덱싱과 슬라이싱


# 인덱싱
# 인덱싱은 문자열에서 각 문자들의 위치에 따른 번호를 매겼을 때 그 번호를 대입하면 해당하는 문자를 반환하는 것을 말한다.

a = 'hi my name is jiwon'
print(a[3]) # 문자열[문자 위치의 번호]로 사용한다. 이때 문자열은 0123456... 순으로 문자에 순서를 매긴다.

# 슬라이싱
# 슬라이싱은 문자열[시작번호:끝번호]로 사용하며, 시작번호의 문자부터 끝번호 직전까지의 문자 '사이'의 문자들을 반환한다.
a = 'hi my name is jiwon'
print(a[6:10])
# 번외로
# 문자열[:끝번호] 혹은 문자열[시작번호:]도 사용 가능하다. 그럴경우, 생략된 부분은 모든 문자의 가장 처음 부분이거나 끝부분이 된다.
print(a[:10]) # 처음부터 10까지 반환
print(a[6:]) # 6부터 끝까지 반환