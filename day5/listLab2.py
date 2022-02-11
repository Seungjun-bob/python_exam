listnum = [10, 5, 7, 21, 4, 8, 18]
minnum = listnum[0]

for num in listnum:
    if num < minnum:
        minnum = num

print('최솟값 :', minnum, sep='')