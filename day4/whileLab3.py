import random
# 65 ~ 90
sum = 0

while True:
    num = random.randint(0,30)
    if num == 0 or 27 <= num <= 30:
        break
    else:
        print(chr(64+num), "(%d)"%(num), sep="")
        sum += 1
print("수행횟수는 %d번입니다."%(sum))