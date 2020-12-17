# 딕셔너리는 key:value와 같이 하나의 쌍으로 이루어진 자료형

# 딕셔너리의 선언
number = [3, 7] # 리스트
favorite_number = "좋아하는 숫자"
age = 25 # 정수형
dictionary = {"이름" : "정지원", "좋아하는 것" : ["피아노, 독서"], "나이" : age, favorite_number : number, ("아침식사", "저녁식사") : ["김치찌개", "삼겹살"] } # 이때, key값에는 변할 수 있는 값을 넣을 수 없다. 그러므로 리스트는 넣을 수 없지만, 튜플은 가능하다.
print(dictionary)

# 딕셔너리의 추가
dictionary["좋아하는 과일"] = "사과" # 추가하고자 하는 딕셔너리의 이름[key] = value 의 형식으로 추가한다.
print(dictionary)

# 딕셔너리의 삭제

del dictionary["좋아하는 과일"] # 삭제하고자 하는 딕셔너리의 key값을 []안에 넣으면 그 key와 value가 삭제된다.
print(dictionary)

# 딕셔너리의 값 추출하기
a = dictionary["이름"] # key값을 넣어주면 그 key의 value를 추출해줌 
print(a)

# 이때, 딕셔너리의 요소 중 같은 key값이 을 가진 자료들이 있을 경우, 가장 마지막에 있는 value만 불러진다.
b = {"악기" : "바이올린", "악기" : "피아노"}
print(b)
d = dictionary["악기"]
print(d)