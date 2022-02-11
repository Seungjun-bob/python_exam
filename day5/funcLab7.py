def print_gugudan(num):
    if type(num) != int:
        return print('숫자를 입력해주세요!')
    elif num < 1 or 9 < num:
        return print('9단까지만 입력 가능합니다.')
    else:
        for i in range(1,10):
            print(num, '*', i, '=', num*i)

print_gugudan('가')
print_gugudan(10)
print_gugudan(6)