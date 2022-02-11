listnum = [10, 5, 7, 21, 4, 8, 18]
maxnum = listnum[0]

for num in listnum:
    if maxnum < num:
        maxnum = num

print('최댓값 :', maxnum, sep='')