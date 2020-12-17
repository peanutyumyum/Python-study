# 딕셔너리의 key를 모아둔 리스트를 생성시키는 함수 keys
number = [3, 7] # 리스트
favorite_number = "좋아하는 숫자"
age = 25 # 정수형
dictionary = {"이름" : "정지원", "좋아하는 것" : ["피아노, 독서"], "나이" : age, favorite_number : number, ("아침식사", "저녁식사") : ["김치찌개", "삼겹살"] }
dictionary_keys = dictionary.keys() # dict_keys(딕셔너리 key의 리스트) = 그렇기 때문에 인덱싱이 안됨
print(dictionary_keys)

dictionary_keys_list = list(dictionary_keys) # 이렇게 변환해야함 리스트로 나옴
print(dictionary_keys_list)


# 딕셔너리의 value를 모아둔 리스트를 생성시키는 함수 values
dictionary_values = dictionary.values() # dict_values(딕셔너리 value의 리스트) = 그렇기 때문에 인덱싱이 안됨
print(dictionary_values)

dictionary_values_list = list(dictionary_values) # 이렇게 변환해야함 리스트로 나옴
print(dictionary_values_list)


# 딕셔너리의 key:value 쌍을 튜플로 묶은 리스트를 생성시키는 함수 items
dictionary_itms = dictionary.items() # dict_values([(key, value),(key2, value2)])로 나옴 = 그렇기 때문에 인덱싱이 안됨
print(dictionary_itms)

dictionary_itms_list = list(dictionary_itms) # 이렇게 변환해야함 리스트로 나옴
print(dictionary_itms_list)


# 딕셔너리의 key에 해당하는 value를 반환하는 함수 get
dictionary_get = dictionary.get("이름")
print(dictionary_get)

# 이때, key값이 없을 경우 특정 값을 반환하게 설정 할 수도 있다.
dictionary_get = dictionary.get("대학", "한양대학교 에리카") # 딕셔너리.get("없는 key값", "설정한 값")
print(dictionary_get)


# 찾고자 하는 key 값이 있는지 없는지 확인하여 True 혹은 False를 반환하는 함수 in
dictionary_boolean = "지역" in dictionary # dictionary라는 딕셔너리 안에 "지역"이라는 key 값이 있는지 확인하여 True 혹은 False를 반환
print(dictionary_boolean)


# 딕셔너리의 모든 요소를 삭제하는 함수 clear
dictionary_clear = dictionary.clear() # 딕셔너리의 요소를 모두 삭제하여 none을 반환한다.
print(dictionary_clear)