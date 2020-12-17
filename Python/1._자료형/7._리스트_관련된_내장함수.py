# Python에는 리스트와 관련되 내장함수들이 있다.

# 리스트에 요소를 맨 뒤에 추가해주는 함수 append
a = [1, 2, 3]
a.append(6)
print(a) # 리스트 a의 맨 마지막에 요소를 추가해주는 append를 사용하였다. 정수 6이라는 것을 추가해주었으므로 여기서는 [1, 2, 3, 6]을 반환할 것이다.(하나만 추가할 수 있음)
# or
a = [1, 2, 3]
a.append([7, 8])
print(a) # 또한 리스트를 추가할 수도 있다. [7, 8]이라는 리스트를 추가해주었으므로, 여기서는 [1, 2, 3, [7, 8]]을 반환할 것이다.

# 리스트 요소에 맨 뒤에 값을 꺼내고 꺼낸 값을 삭제해주는 함수 pop
a = [1, 2, 3]
print(a.pop()) # 맨 뒤의 값을 꺼내므로 3을 출력할 것이다.
print(a) # 리스트 a의 맨 마지막 요소인 3을 삭제해주는 pop을 사용하였다. 결과적으로 [1, 2]를 반환할 것이다.

# 리스트 요소를 오름차순(첫번째 순서부터(1, 2, 3... or "a", "b", "c"...))으로 정렬해주는 함수 sort
a = [4, 7, 2]
a.sort()
print(a)
# or
a = ["string", "jiwon"]
a.sort()
print(a)

# 리스트 요소들의 순서를 바꿔주는(역순) 함수 reverse
a = [1, 2, 3]
a.reverse()
print(a)

# 리스트 요소 중 지정 값의 위치를 반환하는 함수 index
a = [1, 2, 3]
b = a.index(2)
print(b)

# 리스트 요소를 지정된 위치에 지정 값을 삽입하는 함수 insert
a = [1, 2, 3]
a.insert(1, 5) # insert(위치, 값)으로 사용한다.
print(a)

# 리스트 요소 중 특정 값을 제거하는 함수 remove 이때, 지정된 값이 리스트 요소 중에 다수 존재할 경우 가장 첫 순서의 값만 제거된다.
a = [1, 2, 3, 1, 1, 2]
a.remove(1)
print(a)

# 리스트를 합쳐주는 함수 extend
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b) # a의 리스트 뒤에 b의 모든 리스트 요소들을 추가해준다.
print(a)

# 리스트 요소 중 특정 값의 갯수를 찾아주는 함수 count
a = [1, 2, 3, 1, 1, 2]
b = a.count(1)
print(b)