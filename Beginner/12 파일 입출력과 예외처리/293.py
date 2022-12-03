# 293. py

import csv
f = open("C:/Users/한률/Desktop/VSC/Basic/Beginner/12 파일 입출력과 예외처리/매수종목.csv", mode = "wt", encoding = "cp949", newline = "")
writer = csv.writer(f)
writer.writerow(["종목명", "종목코드", "PER"])
writer.writerow(["삼성전자", "005930", 15.59])
writer.writerow(["NAVER", "035420", 55.82])
f.close()