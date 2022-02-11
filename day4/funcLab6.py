import random


def differtwobalue(num1, num2):
    if num1 < num2:
        return num2 - num1
    elif num2 < num1:
        return num1 - num2
    elif num1 == num2:
        return 0

for _ in range(5):
    a = random.randint(1,30)
    b = random.randint(1,30)
    print("%d 와 %d의 차는 %d 입니다."%(a,b,differtwobalue(a, b)))
