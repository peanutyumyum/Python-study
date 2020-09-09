# 정수, 실수의 연산


# 덧셈
a = 3+2
print(a)

# 곱셈
a = 8*5
print(a)

# 나눗셈
a = 8/5
print(a)

# 몫만 구하는 나눗셈
a = 8//5
print(a)

# 나머지만 구하는 나눗셈
a = 8%5
print(a)

# 제곱
a = 5**3
print(a)


# 위의 연산자를 사용하여 변수 본래의 값에 특정 숫자를 연산해주는 대입연산자를 사용할 수 있다.
# 대입연산자

# 덧셈
a = 3
a += 3
print(a)

# 곱셈
a = 8
a *= 3
print(a)

# 나눗셈
a = 8
a /= 5
print(a)

# 몫만 구하는 나눗셈
a = 8
a //= 5
print(a)

# 나머지만 구하는 나눗셈
a = 8
a %= 5
print(a)

# 제곱
a = 5
a **= 3
print(a)


# 문자열을 정수, 실수로 바꿔주는 함수

# int()함수
a = "1"
int(a) # 정수 자료형으로 바꿔주는 함수
print(a)

# float()함수
a = "1.5"
float(a) # 실수 자료형으로 바꿔주는 함수
print(a)

# eval() 함수
a = "1.5"
eval(a) # 숫자형으로 바꿔주는 함수
print(a)