# with ~ as이용
# with ~ as를 이용하면 close()함수를 이용하지 않아도 됨
with open("C:/Users/jiwon/Desktop/코딩/python-study/Python-study/Python/0._기타/1._읽기,_쓰기.txt", "a") as file_open:
    data = "\n---<< 추가내용 >>---\n"
    file_open.write(data)

    for cnt in range(11, 16):
        add_wrt = " >> %02d 회 동계올림픽\n" % cnt
        file_open.write(add_wrt)