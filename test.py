import csv

#r - 읽기모드, 파일이 없으면 Error
#r+ - 읽기 쓰기 모두가능, 파일이 없으면 Error
#w - 쓰기모드, 파일이 없으면 새로만듬
#w+ - 읽기 쓰기 모두가능, 파일이 없으면 새로만듬
#a - 파일 추가, 파일이 없으면 새로 만듬
#a+ - 읽기 쓰기 모두 가능, 파일이 없으면 새로 만듬.
#f = open("text.csv", "a+", encoding='utf-8', newline = "")
#csv_w = csv.writer(f)
#csv_w.writerow(["이름", "이메일","전화번호"])
#f.close()




f2 = open("test.csv", "r", encoding="utf-8")
csv_r = csv.reader(f2)
for line in csv_r:
    print(line)
f2.close()


import os
os.getenv("NAVER_ID")
