import os
import datetime

if os.path.exists("c:/iotest"):
   pass
else:
   os.mkdir("c:/iotest")

m = ['월', '화', '수', '목', '금', '토', '일']
now = datetime.datetime.now()
f = open('c:/iotest/today.txt', 'w', encoding="UTF-8")
f.write(f"오늘은 {now.year}년 {now.month}월 {now.day}일입니다.\n")
f.write(f"오늘은 {m[now.weekday()]}요일입니다.\n")
f.write(f"나는 {m[datetime.datetime(1996, 1, 5).weekday()]}요일에 태어났습니다.\n")
print("저장이 완료되었습니다.")
f.close()