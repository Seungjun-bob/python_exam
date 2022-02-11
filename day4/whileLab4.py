while True:
    month = int(input("1~12 사이의 값을 입력하세요 : "))

    if 1 <= month <= 2 or month == 12:
        print("%d월은 겨울"%(month))
    elif 3 <= month <= 5:
        print("%d월은 봄"%(month))
    elif 6 <= month <= 8:
        print("%d월은 여름"%(month))
    elif 9 <= month <= 11:
        print("%d월은 가을"%(month))
    else:
        print("1~12 사이의 값을 입력하세요!")
        break