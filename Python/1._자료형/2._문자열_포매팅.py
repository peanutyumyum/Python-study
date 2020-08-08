# 포매팅(formatting)은 문자열 안에서 특정 문자만을 바꾸거나 삽입하는 방법이다.


# 숫자의 포매팅
a = "I have %d apple" % 3 # 숫자의 포매팅은 %d를 이용한다.
print(a)

# 문자의 포매팅
a = "I have %s apple" % "three" # 문자의 포매팅은 %s를 이용한다.
print(a)

# 추가적으로 변수를 사용하여 포매팅 할 수도 있다.
number = 3
a = "I have %d apple" % number # 변수를 사용하여 포매팅 하였다.
print(a)

# 게다가 2개 이상의 값을 포매팅 할 수도 있다.
number_apple = 3
number_melon = 4
a = "I have %d apple. and I have %d melon" % (number_apple, number_melon) # 2개 이상의 같은 종류의 자료(숫자, 숫자)를 포매팅 하였다.
print(a)
# or
number_d = 3
number_s = "three"
a = "I have %d apple. and I can eat %s apple" % (number_d, number_s) # 2개 이상의 다른 종류의 자료(숫자, 문자)를 포매팅 하였다.
print(a)