import random

oper_num = random.randint(1, 10)

if oper_num == 1 or oper_num == 6:
    x = 300 + 50
if oper_num == 2 or oper_num == 7:
    x = 300 - 50
if oper_num == 3 or oper_num == 8:
    x = 300 * 50
if oper_num == 4 or oper_num == 9:
    x = 300 / 50
if oper_num == 5 or oper_num == 10:
    x = 300 // 50
print("결과값 : " + str(x))