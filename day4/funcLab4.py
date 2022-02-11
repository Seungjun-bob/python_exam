def print_triangle(num):
    if 1 <= num <= 10:
        for i in range(1, num+1):
            print("*"*(i))
    else:
        return

print_triangle(9)
print_triangle(4)
print_triangle(0)
