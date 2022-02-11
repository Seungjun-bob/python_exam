import random

lst = [random.randint(0,100) for _ in range(10)]
dic = { i : 'pass' if i >= 60 else "nopass" for i in lst}

print(lst)
print(dic)