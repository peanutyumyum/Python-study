"=============================================================================================================================="

# 파일 읽기
# r은 읽기모드이다.
file_open = open("C:/Users/jiwon/Desktop/코딩/python-study/Python-study/Python/0._기타/1._읽기,_쓰기.txt", "r")

while True:
    all_line = file_open.readlines() # readlines는 한줄 한줄 리스트로 만들어 반환한다.
    for cnt in all_line:
        print(cnt)

file_open.close()