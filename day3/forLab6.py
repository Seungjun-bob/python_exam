evenNum, oddNum = 0, 0

for i in range(1,101):
    if i % 2 == 0:
        evenNum += i
    else:
        oddNum += i
print("""
1부터 100까지의 숫자들 중에서
짝수의 합은 %d 이고
홀수의 합은 %d 이다."""%(evenNum, oddNum)
      )
