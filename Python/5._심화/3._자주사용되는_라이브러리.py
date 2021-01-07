"""
모듈과 관련된 상세한 조작법은 필요할 때 구글링하여 사용해보쟈!
"""


# time
"""
시간과 관련된 모듈
"""

import time
print(time.time())

for i in range(5):
    print(i)
    time.sleep(1)
    "여기서 쓰이는 time.sleep은 일정한 시간을 기다리는 것이다 이를 이용하면 프로그램의 동작 시간을 조정할 수 있다ㅛ"


# calendar
"""
달력을 보여주는 모듈
"""
import calendar
print(calendar.calendar(2021))


# random
"""
임의의 수를 발생시키는 모듈
"""
import random
print(random.random())


# webbrowser
"""
자신의 시스템이 사용하는 기본 웹 브라우저를 자동으로 실행하는 모듈
"""
import webbrowser
webbrowser.open("https://naver.com")