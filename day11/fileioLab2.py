f = open('sample.txt', 'r', encoding='utf-8')
lines = f.readlines()
f.close()

f = open('sample_2022_02_13.txt', 'a')
for line in lines:
    f.write(line.strip()+'\n')
print("저장이 완료되었습니다.")
f.close()
