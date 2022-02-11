def print_triangle_withdeco(num, deco='%'):
    if num < 1 or num > 10:
        num = 5
    for i in range(num+1):
        print(' '*(num-i) + deco*i)

print_triangle_withdeco(11, '*')
print_triangle_withdeco(5, '%')
print_triangle_withdeco(3, '$')
print_triangle_withdeco(2)
