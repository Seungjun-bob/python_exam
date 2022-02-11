import random

result = 0
start = random.randint(1, 10)
end = random.randint(30, 40)

# print("start:", start, "\n", "end :", end)

for i in range(start, end+1):
    if i % 2 == 0:
        result += i

print("%d 부터 %d 까지의 짝수의 합 :"%(start, end), result)