try:
    f = open('yesterday.txt', 'r')
    lines = f.readlines()
    count = 0
except FileNotFoundError as m:
    print("파일을 읽을 수 없어요")
else:
    for line in lines:
        if 'yesterday' in line.lower():
            count += 1
    print("Number of a Word 'Yesterday'", count)
finally:
    print("수행완료")
f.close()