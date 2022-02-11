def print_triangle(num):
    if 1 <= num <= 10:
        for i in range(num,0,-1):
            print("@"*i)
    else:
        return

print_triangle(5)
print_triangle(2)
print_triangle(0)