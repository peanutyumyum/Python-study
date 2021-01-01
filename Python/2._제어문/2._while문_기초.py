# while
"""
while문은 조건이 참일 때 계속 반복해서 수행된다.
"""
number = 0
while number <= 10:
    number += 1
    print("수행되었습니다")



# break(강제종료)
"""
while문에서 break는 반복 여부와 상관없이 while문을 종료하는 코드이다.
밑에 쓰여져 있는 코드는 실행되지 않고 무조건 종료된다.
"""
time = 0
while True:
    print("실행중")
    if time >= 5:
        break
    else:
        time += 1


# continue(다시 되돌아가기)
"""
while문에서 continue는 무조건 while문을 다시 시작한다.
이때, 코드를 다시 시작한다는 것이지, 그 전까지 시행되었던 조건을 초기화 시키고 다시 시작한다는 뜻은 아니다.
밑에 쓰여져 있는 코드는 실행되지 않고 무조건 while문을 처음 시작한다.
"""

a = 0
while a <10:
    a += 1
    if a % 2 == 0:
        continue
    else:
        print(a)