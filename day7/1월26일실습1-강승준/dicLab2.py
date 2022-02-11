days = { "월": (5, -3),
         "화": (2, -8),
         "수": (7, -7),
         "목": (4, -7),
         "금": (3, -8),
         "토": (2, -9),
         "일": (4, -8)
        }

day = input("요일명을 한글로 입력하세요 :")
if day in days.keys():
    print(day, "요일의 최저온도는", min(days[day]), "이고 최고 온도는 ",
          max(days[day]),"입니다", sep="")
else:
    print(day, "요일의 정보를 찾을 수 없습니다.", sep="")