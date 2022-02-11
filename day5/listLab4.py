import random

listnum = [random.randint(1, 50) for _ in range(10)]
print(listnum)
# ---------------------------------------------------
for i in listnum:
    if i < 10:
        listnum[listnum.index(i)] = 100
print(listnum)
# ---------------------------------------------------
print(listnum[0])
print(listnum[-1])
print(listnum[1:6])
print(listnum[::-1])
print(listnum[::])
del(listnum[4])  # 5번쨰 삭제
print(listnum)
del(listnum[1:3])  # 2,3번째 삭제
print(listnum)