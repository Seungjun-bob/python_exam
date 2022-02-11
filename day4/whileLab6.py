while True:
    num = int(input("입력값 :"))

    if num == 0:
        print("종료")
        break
    elif num < -10 or 10 < num:
        continue
    elif num > 0:
        print("입력값 :%d"%(num))
        result = 1
        for i in range(1, num+1):
            result *= i
        print(result)
    elif num < 0:
        num = -num
        print("입력값(부호변경) :%d"%(num))
        result = 1
        for i in range(1, num+1):
            result *= i
        print(result)