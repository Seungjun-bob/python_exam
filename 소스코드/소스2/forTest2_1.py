# 1부터 30까지의 정수숫자들중에서 3의 배수는 "3의 배수입니다."
# 아니면 "3의 배수가 아닙니다."를 출력하자.
for v in range(1,31):
    if v % 3 == 0 :
        print(v, ": 3의 배수입니다.")
    else :
        print(v, ": 3의 배수가 아닙니다.")