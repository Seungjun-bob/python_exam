def expr(num1, num2, op):
    if op == '+':
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        result = num1 / num2
    else:
        return None
    return result

temp = expr(20,4,'/')

if temp == None:
    print("수행 불가")
else:
    print("연산결과 :", temp, sep="")
