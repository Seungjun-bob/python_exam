listnum = [10, 5, 7, 21, 4, 8, 18]
maxnum = listnum[0]
minnum = listnum[0]
for num in listnum:
    if maxnum < num:
        maxnum = num
    if num < minnum:
        minnum = num


print('최솟값 :%d, 최댓값: %d'%(minnum, maxnum))