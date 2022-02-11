def number_all_sum(*p):
    sum = 0
    intnum = 0
    if len(p) == 0:
        return
    for data in p:
        if type(data) == int:
            sum += data
            intnum += 1
    if intnum == 0:
        return
    return sum

print(number_all_sum(1,2,3,4,5))
print(number_all_sum(1,2,'a',3,4,'b',5))
print(number_all_sum(10,20,True))
print(number_all_sum())
print(number_all_sum('a',True,'가'))