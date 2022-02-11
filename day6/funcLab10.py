def sumeven(*p):
    result = 0
    if len(p) == 0:
        return -1
    for data in p:
        if data % 2 == 0:
            result += data

    return result

print(sumeven(1,2,3,4,5))
print(sumeven(11,22,33,44,55))
print(sumeven(1,3,5))
print(sumeven())