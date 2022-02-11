array = [[0]*4 for i in range(4)]

cnt = 10
for i in range(4):
    for j in range(4):
        array[i][j] = cnt
        cnt += 2

print(array)
print("1행 1열의 데이터 :", array[0][0])
print("3행 4열의 데이터 :", array[2][3])
print("행의 갯수 :", len(array))
print("열의 갯수 :", len(array[0]))
print("3행의 데이터들 :", ' '.join(map(str, array[2])))
print("2열의 데이터들 :", ' '.join(map(str, [i[1] for i in array])))
print("왼쪽 대각선 데이터들 :", ' '.join(map(str, [array[i][i] for i in range(4)])))

r_data = []
for i in range(4):
    j = 4-i-1
    r_data.append(array[i][j])

print("오른쪽 대각선 데이터들 :", ' '.join(map(str, r_data)))