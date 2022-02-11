from collections import Counter
lst = [['B','C','A','A'],['C','C','B','B'],['D','A','A','D']]

Anum = 0
Bnum = 0
Cnum = 0
Dnum = 0
for i in lst:
    for j in i:
        if j == "A":
            Anum += 1
        elif j == "B":
            Bnum += 1
        elif j == "C":
            Cnum += 1
        elif j == "D":
            Dnum += 1
cntlst = [Anum, Bnum, Cnum, Dnum]

print("A 는 %d개 입니다."%(cntlst[0]))
print("B 는 %d개 입니다."%(cntlst[1]))
print("C 는 %d개 입니다."%(cntlst[2]))
print("D 는 %d개 입니다."%(cntlst[3]))
