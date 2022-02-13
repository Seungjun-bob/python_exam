import calendar

while True:
    try:
        year = int(input("년도 :"))
        month = int(input("월 :"))
    except ValueError as m:
        print("숫자를 입력해주세요.")
    else:
        print(calendar.month(year, month))
        break