import random

set1 = set()
while len(set1)<6:
    set1.add(random.randint(1,45))

set1_new = [str(a) for a in set1]
print("행운의 로또번호 :", ','.join(set1_new), sep='')