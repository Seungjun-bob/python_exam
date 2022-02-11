import random

while True:
    pairNum1 = random.randint(1, 6)
    pairNum2 = random.randint(1, 6)

    if pairNum1 < pairNum2:
        print("%d이 %d보다 크다."%(pairNum2, pairNum1))
    elif pairNum2 < pairNum1:
        print("%d이 %d보다 크다."%(pairNum1, pairNum2))
    else:
        print("게임 끝")
        break
