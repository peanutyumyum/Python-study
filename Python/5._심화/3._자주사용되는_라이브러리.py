"""
모듈과 관련된 상세한 조작법은 필요할 때 구글링하여 사용해보쟈!
"""

#os
"""
os모듈은 Operating System의 약자로 운영체제에서 사용되는 여러 기능을 파이썬에서 사용할 수 있게끔 해준다
예를 들면 파일을 복사하거나, 디렉터리를 생성하고 특정 디렉터리 내의 파일 목록을 구하고자 할 때 사용된다
"""
import os
print(os.getcwd())

# os.path.dirname() 모듈
"내가 지정한 경로의 파일 혹은 폴더의 디렉터리 값을 가져오는 함수"
dirname = os.path.dirname("C:/Users/jiwon/Desktop/ex/Hackathon_Lionders")
print(dirname)



# time
"""
시간과 관련된 모듈
"""

import time
print(time.time())

for i in range(5):
    print(i)
    time.sleep(1)
    "여기서 쓰이는 time.sleep은 일정한 시간을 기다리는 것이다 이를 이용하면 프로그램의 동작 시간을 조정할 수 있다"


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