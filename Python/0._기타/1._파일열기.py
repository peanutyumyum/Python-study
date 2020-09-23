# 파일 쓰기
# w는 쓰기모드이다.
file_open = open("C:/Users/jiwon/Desktop/코딩/python-study/Python-study/Python/0._기타/1._읽기,_쓰기.txt", "w")

for num in range(0, 11):
    prt = " >> %02d 회 동계올림픽\n" % num
    file_open.write(prt)

file_open.close()
# 코드 실행 후 해당 경로로 가면 txt파일이 생성되어 있을 것이다.