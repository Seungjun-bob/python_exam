s1 = "pythonjavascript"
print(len(s1))

s2 = "010-7777-9999"
print(''.join(s2.split('-')))

s3 = "PYTHON"
print(''.join(reversed(s3)))

s4 = "Python"
print(s4.lower())

s5 = "https://www.python.org/"
s5 = s5.replace("https://", "")
s5 = s5.replace("/", "")
print(s5)

s6 = '891022-2473837'
if s6[7] == 1 or s6[7] == 3:
    print("남성")
else:
    print("여성")

s7 = '100'
print("정수형 :", int(s7), "실수형 :", float(s7))

s8 = 'The Zen of Python'
answer = 0
for i in s8:
    if i =='n':
        answer +=1
print("n의 개수 :", answer)

print("Z의 위치 :", s8.find("Z"))

print(s8.upper().split(" "))